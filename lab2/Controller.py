from Configuration import Configuration


class Controller:
    def __init__(self, problem):
        self.__problem = problem

    def DFS(self, root, n):
        if root.isFinal():
            return root
        else:
            for i in range(0, n):
                if root.isSafe(i):
                    root.nextConfig(i)
                    res = self.DFS(root, n)
                    if res is not None:
                        return res
                    root.emptyPlace()

        return None

    def greedy(self, root, n):
        if root.isFinal():
            return root
        else:
            allConfigs = dict()
            for i in range(0, n):
                if root.isSafe(i):
                    root.nextConfig(i)
                    allConfigs[root.getValidPlaces] = root.getConfigValues()
            root = Configuration(allConfigs.get(sorted(allConfigs.keys())[0]))
            res = self.DFS(root, n)
            if res is not None:
                return res

            root.emptyPlace()

        return None