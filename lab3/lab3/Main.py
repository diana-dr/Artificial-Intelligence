from EA import *
from HC import *
from PSO import *


def main(iterations=1000):

    n = int(input("Enter number of elements : "))
    set1 = list(map(int, input("Enter first set: ").strip().split()))[:n]
    set2 = list(map(int, input("Enter second set: ").strip().split()))[:n]

    print("Menu")
    print("0. EXIT")
    print("1. Evolutionary Algorithm")
    print("2. Hill Climbing")
    print("3. Particle Swarm Optimisation")

    number = 1

    while number != 0:
        number = int(input("Choose Method: "))
        if number == 1:
            runEA(iterations, set1, set2)
        elif number == 2:
            runHC(iterations, set1, set2)
        elif number == 3:
            runPSO(iterations, set1, set2)


main()
