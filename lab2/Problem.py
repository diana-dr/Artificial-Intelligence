from State import State


class Problem:
    def __init__(self,initial):
        self.__initialConfig = initial
        self.__initialState = State()
        self.__initialState.setValues([initial])

    def expand(self, currentState):
        myList = []
        currentConfig = currentState.getValues()[-1]
        for j in range(currentConfig.getSize()):
            for x in currentConfig.nextConfig(j):
                myList.append(currentState + x)
        return myList

    def getRoot(self):
        return self.__initialConfig