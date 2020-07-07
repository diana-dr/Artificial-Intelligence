import random
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def Main():
    data = pd.read_csv('data.txt', names=["x1", "x2", "x3", "x4", "x5", "y"])
    colums = (data.columns[0])
    max = [data[c].max() for c in data.columns]
    min = [data[c].min() for c in data.columns]
    i = 0
    for c in data.columns:
        while i < len(data.columns):
            data[c] = (data[c] - min[i]) / (max[i] - min[i])
            i = i + 1
            break

    arr = data.values
    x_train = []
    y = []
    a = data.shape
    for i in range(a[0]):
        x_train.append((arr[i][:-1]).tolist())
        y.append(arr[i][-1])

    m = np.ones((497, 1))
    b = np.matrix(x_train)
    b = np.concatenate((m, b), axis=1)
    d = b.T
    e = np.linalg.inv(np.matmul(d, b))
    y = np.matrix(y)
    y = y.T
    f = np.matmul(e, d)
    c = np.matmul(f, y)

    x_test = [[1], ]
    for j in range(5):
        # inp = [float(input("Enter Value:"))]
        inp = [random.random()]
        x_test.append(inp)
    for i in range(5):
        x_test[i + 1][0] = (x_test[i + 1][0] - min[i]) / (max[i] - min[i])
    x_test = np.matrix(x_test)
    Y = np.matmul(c.T, x_test)

    print((Y*(max[-1]-min[-1]))+min[-1])

Main()