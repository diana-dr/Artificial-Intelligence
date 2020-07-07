from math import *

import numpy as np
import matplotlib.pyplot as plt

from NeuralNetwork import NeuralNetwork


def readData(fileName):

    inData= []
    outData = []
    noFeatures = 0
    noOutputs = 1
    with open(fileName) as f:
        lines = f.readlines()
        noExamples = len(lines)
        for line in lines:
            line = line.rstrip()
            data = line.split(' ')
            noFeatures = len(data) - 1
            if len(data) < 6:
                continue
            inp = []
            for i in range(len(data) - 1):
                inp.append(float(data[i]))
            outData.append(float(data[-1]))
            inData.append(inp)

    return noExamples, noFeatures, noOutputs, inData, outData


def normaliseData(noExamples, noFeatures, trainData, noTestExamples, testData):
    for j in range(noFeatures):
        summ = 0.0
        for i in range(noExamples):
            summ += trainData[i][j]
        mean = summ / noExamples
        squareSum = 0.0
        for i in range(noExamples):
            squareSum += (trainData[i][j] - mean) ** 2
        deviation = sqrt(squareSum / noExamples)
        for i in range(noExamples):
            trainData[i][j] = (trainData[i][j] - mean) / deviation
        for i in range(noTestExamples):
            testData[i][j] = (testData[i][j] - mean) / deviation


def devise_data():
    res1 = readData("data.txt")

    inTestData = []
    outTestData = []

    inTrainData = []
    outTrainData = []
    for i in range(len(res1[3])):
        if i % 10 == 0:
            inTestData.append(res1[3][i])
            outTestData.append(res1[4][i])
        else:
            inTrainData.append(res1[3][i])
            outTrainData.append(res1[4][i])

    normaliseData(len(inTrainData), res1[1], inTrainData, len(inTestData), inTestData)

    return inTrainData, outTrainData, inTestData, outTestData


def Main():
    result = devise_data()

    inTrain = np.array(result[0])
    outTrain = np.array(result[1])

    inTest = np.array(result[2])
    outTest = np.array(result[3])

    nn = NeuralNetwork(inTrain, outTrain, 1)

    nn.loss=[]
    iterations =[]
    for i in range(3000):
        nn.feedforward()
        nn.backprop(1)
        iterations.append(i)

    print(nn.output)

    plt.plot(iterations, nn.loss, label='loss value vs iteration')
    plt.xlabel('Iterations')
    plt.ylabel('loss function')
    plt.legend()
    plt.show()

    test = NeuralNetwork(inTest, outTest, 1)

    test.loss = []
    iterations = []
    for i in range(3000):
        test.feedforward()
        test.backprop(1)
        iterations.append(i)

    print(test.output)

    plt.plot(iterations, test.loss, label='loss value vs iteration')
    plt.xlabel('Iterations')
    plt.ylabel('loss function')
    plt.legend()
    plt.show()

Main()