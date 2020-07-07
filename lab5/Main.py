from Controller import *


def main():
    alpha = 1.9
    beta = 0.9
    rho = 0.05
    q0 = 0.5

    n = int(input("Enter number of elements : "))
    set1 = list(map(int, input("Enter first set: ").strip().split()))[:n]
    set2 = list(map(int, input("Enter second set: ").strip().split()))[:n]

    lst = []
    for i in set1:
        for j in set2:
            lst.append((i, j))

    ctrl = Controller(n, alpha, beta, q0, rho, lst)
    bestSol = ctrl.runAlg()
    print("Solution Found!")
    for line in bestSol:
        print(line)


main()