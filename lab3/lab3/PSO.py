from EA import individual, fitness
import random


class Particle:
    """ The class that implements a particle """

    def __init__(self, l, set1, set2):
        self._position = individual(set1, set2)
        self._fitness = self.fit()
        self.velocity = [0 for i in range(l)]

        self._bestPosition = self._position.copy()
        self._bestFitness = self._fitness

    def fit(self):
        ft = 0
        matrix = self._position
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                value = matrix[i][j]
                for k in range(len(matrix)):
                    for l in range(len(matrix)):
                        if value == matrix[k][l] and (i != k or j != l):
                            ft += 1
        return int(ft / 2)

    def evaluate(self):
        """ evaluates the particle """
        self._fitness = self.fit()

    @property
    def position(self):
        """ getter for position """
        return self._position

    @property
    def fitness(self):
        """ getter for fitness """
        return self._fitness

    @property
    def bestPosition(self):
        """ getter for best position """
        return self._bestPosition

    @property
    def bestFitness(self):
        """getter for best fitness """
        return self._bestFitness

    @position.setter
    def position(self, newPosition):
        self._position = newPosition.copy()
        self.evaluate()
        if self._fitness < self._bestFitness:
            self._bestPosition = self._position
            self._bestFitness = self._fitness


def diff(individual1, individual2):
    suma = 0
    # print(individual2)
    # print(individual1)
    # for line1 in individual1:
    #     for line2 in individual2:
    #         suma += sum(pair[0] for pair in line1)
    #         suma += sum(pair[1] for pair in line1)
    #         suma -= sum(pair[0] for pair in line2)
    #         suma -= sum(pair[1] for pair in line2)
    return suma


def population(count, l, set1, set2):

    return [Particle(l, set1, set2) for x in range(count)]


def selectNeighbours(pop, nSize, set1, set2):

    if nSize > len(pop):
        nSize = len(pop)

    neighbours = []
    for i in range(len(pop)):
        localNeighbour = []
        for j in range(nSize):
            x = individual(set1, set2)
            localNeighbour.append(x)
        neighbours.append(localNeighbour.copy())
    return neighbours


def iteration(pop, neighbours, c1, c2, w):
    bestNeighbours = []

    for i in range(len(pop)):
        bestNeighbours.append(neighbours[i][0])
        for j in range(1, len(neighbours[i])):
            if fitness(bestNeighbours[i]) > fitness(neighbours[i][j]):
                bestNeighbours[i] = neighbours[i][j]

    for i in range(len(pop)):
        for j in range(len(pop[0].velocity)):
            newVelocity = w * pop[i].velocity[j]
            newVelocity = newVelocity + c1 * random.random() * diff(bestNeighbours[i], pop[i].position)
            newVelocity = newVelocity + c2 * random.random() * diff(pop[i].bestPosition[j], pop[i].position)
            pop[i].velocity[j] = newVelocity

    for i in range(len(pop)):
        new_position = pop[i].position
        pop[i].position = new_position
    return pop


def runPSO(noIteratii, set1, set2):

    noParticles = int(input("Choose number of particles: "))
    dimParticle = len(set1)

    # specific parameters for PSO
    w = 1.0
    c1 = 1.0
    c2 = 2.5

    sizeOfNeighbourhood = int(input("Choose size of neighbourhood: "))
    pop = population(noParticles, dimParticle, set1, set2)
    neighbourhoods = selectNeighbours(pop, sizeOfNeighbourhood, set1, set2)

    for i in range(noIteratii):
        pop = iteration(pop, neighbourhoods, c1, c2, w / (i + 1))

    best = 0
    for i in range(1, len(pop)):
        if pop[i].fitness < pop[best].fitness:
            best = i

    individual = pop[best].position
    print("Best individual found:")
    for line in individual:
        print(line)
