from math import sqrt
import matplotlib.pyplot as plt
from Controller import *


def findBest():
    alpha = 1.9
    beta = 0.9
    rho = 0.05
    q0 = 0.5
    iterations = 1000
    times = 30
    fit = []
    n = 3
    set1 = [1, 2, 3, 4, 5, 6]
    set2 = [1, 2, 3, 4, 5, 6]
    lst = []
    for i in set1:
        for j in set2:
            lst.append((i, j))

    ctrl = Controller(n, alpha, beta, q0, rho, lst)

    for x in range(times):
        fit = []
        bestSol = ctrl.iteration().copy()
        best = fitness(bestSol)
        for y in range(iterations):
            sol = ctrl.iteration().copy()
            if fitness(sol) < fitness(bestSol):
                best = fitness(sol)
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


def test():
    best = findBest()
    avg = avgDeviation(best)
    std = standardDeviation(best)

    print("Standard deviation: " + str(std))
    print("Average deviation: " + str(avg))

    plt.plot(best)
    plt.ylabel("Fitness variation")
    plt.show()

test()