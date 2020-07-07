import random


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


def intermediate_fitness(matrix, tuple):
    fitness = 1

    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][j] == tuple:
                fitness += 1
    return fitness


class Ant:
    def __init__(self, n, possibilities):
        self.n = n
        self.possibilities = possibilities
        self.size = len(possibilities)
        self.pheromones = [0 for x in range(self.size)]
        self.path = [[(0, 0) for i in range(self.n)] for i in range(self.n)]

    def find_next_free(self):
        for i in range(self.n):
            for j in range(self.n):
                if self.path[i][j] == (0, 0):
                    return i, j

    def nextMoves(self):
        return self.possibilities

    def addMove(self, q0, trace, alpha, beta):
        sm = 0

        x, y = self.find_next_free()
        fitnesses = [intermediate_fitness(self.path, self.possibilities[x]) for x in range(self.size)]
        self.pheromones = [1 / fitnesses[x] for x in range(self.size)]

        for i in range(self.size):
            sm += self.pheromones[i] ** alpha * fitnesses[i] ** beta

        probabilities = [self.pheromones[x] ** alpha * fitnesses[x] ** beta / sm for x in range(self.size)]

        cumulative = []
        for i in range(self.size):
            sum = 0
            for j in range(i, self.size):
                sum += probabilities[j]
            cumulative.append(sum)

        r = random.random()

        if r < q0:
            pairs = [[fitnesses[i], self.possibilities[i]] for i in range(self.size)]
            minim = [pairs[0][0], 0]
            for i in range(1, self.size):
                if pairs[i][0] < minim[0]:
                    minim = [pairs[i][0], i]
            self.path[x][y] = self.possibilities[minim[1]]
        
        else:
            r = random.uniform(0, 1)
            for i in range(self.size):
                if r > cumulative[1]:
                    self.path[x][y] = self.possibilities[0]
                elif r < cumulative[self.size - 1]:
                    self.path[x][y] = self.possibilities[-1]
                else:
                    if cumulative[i] >= r > cumulative[i + 1]:
                        self.path[x][y] = self.possibilities[i]