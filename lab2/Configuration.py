class Configuration:

    def __init__(self, positions):
        self.__size = len(positions)
        self.__values = positions[:]
        self.__count = 0

    def getConfigSize(self):
        return self.__size

    def getConfigValues(self):
        return self.__values

    def isFullConfig(self):
        zeros = 0
        for i in self.__values:
            if i == -1:
                zeros += 1
        return zeros == 0

    def nextConfig(self,j):
        if 0 <= j < self.__size:
            self.__values[self.__count] = j
            self.__count += 1
        return self.__values

    def isFinal(self):
        if self.__size == self.__count:
            return True
        else:
            return False

    def __len__(self):
        return len(self.__values)

    def emptyPlace(self):
        if self.__count > 0:
            self.__count -= 1

    def isSafe(self,j):
        for i in range(self.__count):
            if self.__values[i] == j or abs(j-self.__values[i]) == self.__count-i:
                return False
        return True

    def getValidPlaces(self):
        safeSpaces = 0
        for j in range(self.__count):
            for i in range(self.__count):
                if self.__values[i] == j or abs(j - self.__values[i]) == self.__count - i:
                    continue
                safeSpaces += 1
        return safeSpaces

    def __str__(self):
        return str(self.__values)