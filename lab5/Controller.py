from Ant import *


class Controller:
    def __init__(self, n, alpha, beta, q0, rho, lst):
        self.noAnts = 3
        self.trace = [[1 for i in range(n * n)] for j in range(n * n)]
        self.n = n
        self.alpha = alpha
        self.beta = beta
        self.q0 = q0
        self.rho = rho
        self.lst = lst

    def iteration(self):
        antSet = [Ant(self.n, self.lst) for i in range(self.noAnts)]
        for i in range(self.n * self.n):
            for x in antSet:
                x.addMove(self.q0, self.trace, self.alpha, self.beta)
        dTrace = [1.0 / intermediate_fitness(antSet[i].path, antSet[i]) for i in range(len(antSet))]
        for i in range(self.n * self.n):
            for j in range(self.n * self.n):
                self.trace[i][j] = (1 - self.rho) * self.trace[i][j]
        for i in range(len(antSet)):
            for j in range(len(antSet[i].path) - 1):
                x = int(antSet[i].pheromones[j])
                y = int(antSet[i].pheromones[j + 1])
                self.trace[x][y] = self.trace[x][y] + dTrace[i]
        f = [[intermediate_fitness(antSet[i].path, antSet[i]), i] for i in range(len(antSet))]
        f = min(f)
        return antSet[f[1]].path

    def runAlg(self):
        bestSol = self.iteration().copy()

        while fitness(bestSol) != 0:
            sol = self.iteration().copy()
            if fitness(sol) < fitness(bestSol):
                bestSol = sol.copy()
        return bestSol
