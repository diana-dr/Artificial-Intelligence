from itertools import permutations
import random


def population(set1, set2, count):
    return [individual(set1, set2) for x in range(count)]


def isSolution(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            value = matrix[i][j]
            for k in range(len(matrix)):
                for l in range(len(matrix)):
                    if value == matrix[k][l] and (i != k or j != l):
                        return False
    return True


def individual(set1, set2):
    number = len(set1)
    matrix = [[(0, 0) for i in range(number)] for i in range(number)]

    list1 = []
    list2 = []
    nb = 0

    for i in range(number):
        list1 += random.choice(list(permutations(set1)))
        list2 += random.choice(list(permutations(set2)))

    for i in range(number):
        for j in range(number):
            matrix[i][j] = (list1[nb], list2[nb])
            nb += 1

    return matrix


def crossover(parent1, parent2):
    child = [[(0,0) for i in range(len(parent1))] for i in range(len(parent1))]

    for i in range(len(parent1)):
        for j in range(len(parent1)):
            if i < len(parent1) / 2 and j <= len(parent1) / 2:
                child[i][j] = parent1[i][j]
            else:
                child[i][j] = parent2[i][j]
    return child


def fitness(matrix):

    fit = 0

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            value = matrix[i][j]
            for k in range(len(matrix)):
                for l in range(len(matrix)):
                    if value == matrix[k][l] and (i != k or j != l):
                        fit += 1

    return int(fit/2)


def mutate(individual, probMut):
    length = len(individual)
    matrix = [[(0,0) for i in range(length)] for i in range(length)]

    for i in range(length):
        for j in range(length):
            if i != j and probMut > random.random():
                matrix[i][j] = individual[j][i]
            else:
                matrix[i][j] = individual[i][j]

    return matrix


def iteration(population, probMut):
    i1 = random.randint(0, len(population) - 1)
    i2 = random.randint(0, len(population) - 1)

    if i1 != i2:

        c = crossover(population[i1], population[i2])
        c = mutate(c, probMut)
        f1 = fitness(population[i1])
        f2 = fitness(population[i2])
        fc = fitness(c)

        if(f1 > f2) and (f1 > fc):
            population[i1] = c

        if(f2 > f1) and (f2 > fc):
            population[i2] = c

    return population


def runEA(iterations, set1, set2):
    size = int(input("Enter population size : "))

    pop = population(set1, set2, size)

    for x in range(iterations):
        pop = iteration(pop, 0.5)
        for i in pop:
            if isSolution(i):
                print("Solution found!")
                for line in i:
                    print(line)
                exit(0)
    print("No solution found!")
    fitness = 0