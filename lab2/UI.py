from time import time
from Controller import Controller
from Problem import Problem
from Configuration import Configuration


class UI:
    def __init__(self):
        self.__initC = Configuration([-1] * 4)
        self.__p = Problem(self.__initC)
        self.__ctrl = Controller(self.__p)
        self.__n = 4

    def printMenu(self):
        str = ''
        str += "0 - exit \n"
        str += "1 - read the number of queens \n"
        str += "2 - find a solution with DFS \n"
        str += "3 - find a soultion with Greedy \n"
        print(str)

    def readCommand(self):
        n = 4
        try:
            print("Input the number of queens")
            n = int(input("n = "))
        except:
            print("Invalid number, the implicit value is 4.")
            n = 4
        self.__initC = Configuration([-1] * n)
        self.__p = Problem(self.__initC)
        self.__ctrl = Controller(self.__p)
        self.__n = n

    def findSolDFS(self):
        startClock = time()
        print(str(self.__ctrl.DFS(self.__p.getRoot(), self.__n)))
        print('execution time = ', time() - startClock, " seconds")

    def findSolGreedy(self):
        startClock = time()
        print(str(self.__ctrl.greedy(self.__p.getRoot(), self.__n)))
        print('execution time = ', time() - startClock, " seconds")

    def run(self):
        run = True
        self.printMenu()
        while run:
            try:
                command = int(input(">> "))
                if command == 0:
                    run = False
                elif command == 1:
                    self.readCommand()
                elif command == 2:
                    self.findSolDFS()
                elif command == 3:
                    self.findSolGreedy()
            except:
                print("Invalid command!")
