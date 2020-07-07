from EA import *
from HC import *
from PSO import *
from math import sqrt
import matplotlib.pyplot as plt


def findBestEA():
    set1 = [1, 2, 3, 4, 5, 6]
    set2 = [1, 2, 3, 4, 5, 6]

    sizeOfPop = 40
    iterations = 1000
    times = 30
    best = 0
    fit = []

    pop = population(set1, set2, sizeOfPop)

    for x in range(times):
        fit = []
        for y in range(iterations):
            pop = iteration(pop, 0.015)
            best = 0
            for i in range(1, len(pop)):
                if pop[i].fitness < pop[best].fitness:
                    best = i
        fit.append(best)
    return fit


def findBestHC():
    set1 = [1, 2, 3, 4, 5, 6]
    set2 = [1, 2, 3, 4, 5, 6]

    iterations = 1000
    times = 30
    best = []

    for x in range(times):
        fit = []
        ind = individual(set1, set2)
        for y in range(iterations):
            ind = iterationHC(ind, set1, set2)
            fit.append(fitness(ind))
        fit.sort()
        best.append(fit[0])

    return best


def findBestPSO():
    set1 = [1, 2, 3, 4, 5, 6]
    set2 = [1, 2, 3, 4, 5, 6]

    sizeOfPop = 40
    iterations = 1000
    times = 30
    sizeOfNeighbourhood = 20
    best = 0
    fit = []

    pop = population(sizeOfPop, len(set1), set1, set2)
    neighbourhoods = selectNeighbours(pop, sizeOfNeighbourhood, set1, set2)

    w = 1.0
    c1 = 1.0
    c2 = 2.5

    for x in range(times):
        for y in range(iterations):
            pop = iteration(pop, neighbourhoods, c1, c2, w / (y + 1))
            best = 0
            for i in range(1, len(pop)):
                if pop[i].fitness < pop[best].fitness:
                    best = i
        fit.append(best)

    return fit


def avgDeviation(lst):
    sum = 0
    noElems = len(lst)

    for fitness in lst:
        sum += fitness

    mean = sum/noElems

    deviations = 0
    for fitness in lst:
        if fitness > mean:
            deviations += fitness - mean
        else:
            deviations += mean - fitness

    return deviations / noElems


def standardDeviation(lst):
    sum = 0
    new1 = []
    noElems = len(lst)

    for fitness in lst:
        sum += fitness

    mean = sum/noElems
    sum = 0

    for fitness in lst:
        sq = fitness - mean
        sq *= fitness - mean
        new1.append(sq)

    for x in new1:
        sum += x

    return sqrt(sum/noElems)


def testEA():
    best = findBestEA()
    avg = avgDeviation(best)
    std = standardDeviation(best)

    print("Standard deviation: " + str(std))
    print("Average deviation: " + str(avg))

    plt.plot(best)
    plt.ylabel("Fitness variation")
    plt.show()


def testHC():
    best = findBestHC()
    avg = avgDeviation(best)
    std = standardDeviation(best)

    print("Standard deviation: " + str(std))
    print("Average deviation: " + str(avg))

    plt.plot(best)
    plt.ylabel("Fitness variation")
    plt.show()


def testPSO():
    best = findBestPSO()
    avg = avgDeviation(best)
    std = standardDeviation(best)

    print("Standard deviation: " + str(std))
    print("Average deviation: " + str(avg))

    plt.plot(best)
    plt.ylabel("Fitness variation")
    plt.show()
