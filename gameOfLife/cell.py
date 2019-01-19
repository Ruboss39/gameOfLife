class Cell:
    def __init__(self,x,y,alive = False):
        self.__x = x
        self.__y = y
        self.__alive = alive
        self.__data = 0

    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y
    
    def isAlive(self):
        return self.__alive

    def setAlive(self,alive):
        self.__alive = alive

    def setData(self,matrix):
        self.__data = 0
        for i in range(0,3):
            for j in range(0,3):
                if i==1 and j==1:
                    continue
                elif matrix[(self.__x -1 + i)%len(matrix)][(self.__y - 1 + j)%len(matrix)].isAlive(): 
                    self.__data += 1
                    
    def aliveCalculation(self):
        cells = self.__data
        if cells <2:
            self.__alive = False
        elif cells == 3:
            self.__alive = True
        elif cells > 3:
            self.__alive = False
        return self.__alive