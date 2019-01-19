from tkinter import *
from cell import Cell

def setup():
    global master
    global w
    global cellMatrix
    global aliveCells
    master.bind("<Button-1>",f2)
    master.bind("<KeyRelease>",f)
    rowSize = 50
    columnSize = 50
    matrix = []
    data = getData("bomb.txt")

    for i in range(0,rowSize + 2):
        column = []
        for j in range(0,columnSize + 2):
            cell = Cell(i,j)
            column.append(cell)
        matrix.append(column)

    for i in data:
        matrix[i[0]][i[1]].setAlive(True)
        aliveCells.append([i[0],i[1]])
    
    cellMatrix = matrix
    displayMatrix(w,cellMatrix,20,20)
    displayGrid(w,rowSize + 2,columnSize + 2,20,20)

def calculateGen(generations):
    global cellMatrix
    global aliveCells
    width = len(cellMatrix)
    height = len(cellMatrix[0])

    for h in range(0,generations):
        cellSet = set()
        tmpList = []
        for cell in aliveCells:
            for i in range(-1,2):
                for j in range(-1,2):
                    cellSet.add((cell[0] + i,cell[1] + j))

        for cell in cellSet:
            index = [cell[0]%width,cell[1]%height]
            cellMatrix[index[0]][index[1]].setData(cellMatrix)

        for cell in cellSet:
            index = [cell[0]%width,cell[1]%height]
            if cellMatrix[index[0]][index[1]].aliveCalculation():
                tmpList.append(index)
        
        aliveCells = tmpList
    return cellSet

def drawCells(x,y,xoffset = 0, yoffset = 0, pixelSize = 10):
    global cellMatrix
    global aliveCells
    x = int((x - xoffset)/pixelSize)
    y = int((y-yoffset)/pixelSize)
    if x in range(0,len(cellMatrix)) and y in range(0,len(cellMatrix[0])):
        if cellMatrix[x][y].isAlive():
            cellMatrix[x][y].setAlive(False)
            aliveCells.remove([x,y])
        else:
            cellMatrix[x][y].setAlive(True)
            aliveCells.append([x,y])          

def killAllCells():
    global cellMatrix
    for row in cellMatrix:
        for cell in row:
            cell.setAlive(False)
          
def displayMatrix(graphics,matrix,offsetx = 0,offsety = 0,pixelSize = 10):
    global aliveCells
    for i in aliveCells:
        x = i[0]
        y = i[1]
        graphics.create_rectangle(pixelSize*x + offsetx,pixelSize*y + offsety, pixelSize*x + pixelSize + offsetx, pixelSize*y + pixelSize + offsety, fill = "#000000")

def displayGrid(graphics,heigth,width,offsetx = 0,offsety = 0,pixelSize = 10):
    for i in range(0,width +1):
        graphics.create_line(offsetx +i*pixelSize,offsety,offsetx + i*pixelSize, offsety + heigth*pixelSize, fill = "#e2e2e2" )
        graphics.create_line(offsetx,offsety + i*pixelSize,offsetx + width*pixelSize,offsety + i*pixelSize, fill = "#e2e2e2")

def displayCells(graphics,cells,offsetx = 0,offsety = 0, pixelSize = 10):
    for cell in cells:
        x = cell[0]
        y = cell[1]
        graphics.create_rectangle(pixelSize*x + offsetx,pixelSize*y + offsety, pixelSize*x + pixelSize + offsetx, pixelSize*y + pixelSize + offsety,fill = "#ffcdff", outline = "#ffcdff" )

def f(event):
    global w
    global cellMatrix
    clearCanvas()
    cells = calculateGen(1)
    displayCells(w,cells,20,20)
    displayMatrix(w,cellMatrix,20,20)
    displayGrid(w,52,52,20,20)

def f2(event):
    global w
    global cellMatrix
    clearCanvas()
    drawCells(event.x,event.y,20,20)
    displayMatrix(w,cellMatrix,20,20)
    displayGrid(w,52,52,20,20)

def clearCanvas():
    global w
    w.delete("all")

def buttonCall():
    global w
    global cellMatrix
    global aliveCells
    aliveCells = []
    killAllCells()
    clearCanvas()
    displayMatrix(w,cellMatrix,20,20)
    displayGrid(w,52,52,20,20)

def getData(filename):
    f = open(filename,"r")
    data = f.readline()
    locations = []
    while data != "":
        x = int(data.split(" ")[0])
        y = int(data.split(" ")[1].strip("\n"))
        locations.append([x,y])
        data = f.readline()
    return locations

width = 2560
height = 1600

master = Tk()
b = Button(master, text="ClearCanvas", command=buttonCall,bg = "#56b7b1", width = 10, height = 1)
w = Canvas(master, width=width ,height=height)
b.pack()
w.pack()

cellMatrix = []
aliveCells = []

setup()
mainloop()