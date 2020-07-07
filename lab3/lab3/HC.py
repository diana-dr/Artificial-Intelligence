from EA import individual, isSolution
import random


def neighbour(individual, set1, set2):
    length = len(individual)
    n = [[(0, 0) for i in range(length)] for i in range(length)]

    line = random.randint(1, length)
    list1 = []
    list2 = []

    list1 += random.choice(list(permutations(set1)))
    list2 += random.choice(list(permutations(set2)))

    for i in range(length):
        for j in range(length):
            if i == line:
                a = random.choice(list1)
                b = random.choice(list2)
                n[i][j] = (a, b)
            else:
                n[i][j] = individual[i][j]

    return n


def iterationHC(ind, set1, set2):

    n1 = neighbour(ind, set1, set2)

    f1 = fitness(n1)
    f = fitness(ind)

    if f1 < f:
        return n1

    return ind


def runHC(iterations, set1, set2):

    ind = individual(set1, set2)

    for x in range(iterations):
        if isSolution(ind):
            print("Solution found!")
            for line in ind:
                print(line)
            exit(0)
        else:
            ind = iterationHC(ind, set1, set2)
    print("No solution found!")

