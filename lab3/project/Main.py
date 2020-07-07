# -*- coding: utf-8 -*-

from EA import *
from MainWindow import *


def main():
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit( app.exec_() )


def main2(iterations = 100000):
    # probability of mutation and crossover
    # population size
    # number of generations

    size = int(input("Enter population size : "))
    n = int(input("Enter number of elements : "))

    set1 = list(map(int, input("Enter first set: ").strip().split()))[:n]
    set2 = list(map(int, input("Enter second set: ").strip().split()))[:n]

    pop = population(set1, set2, size)

    for x in range(iterations):
        pop = iteration(pop, 0.5)
        for i in pop:
            if (isSolution(i)):
                print("Solution found!")
                for line in i:
                    print(line)
                exit(0)

main()