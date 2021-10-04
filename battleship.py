"""
Battleship Project
Name: Vedavyas Vundyala
Roll No: 2021-IIITH-C1-039
"""

# import battleship_tests as test
import battleship_tests as test
PROJECT = "Battleship" # don't edit this

### SIMULATION FUNCTIONS ###

from tkinter import *
import random

import tkinter as tk

EMPTY_UNCLICKED = 1
SHIP_UNCLICKED = 2
EMPTY_CLICKED = 3
SHIP_CLICKED = 4


'''
makeModel(data)
Parameters: dict mapping strs to values
Returns: None
'''
def makeModel(data):
    data["No fo rows & cols"] = 10
    data["boardSize"] = 500
    data["cellsize"] = data["boardSize"] / data["No fo rows & cols"]
    data["numBoards"] = 2
    data["numShips"] = 5
    data["computerBoard"] = emptyGrid(data["No fo rows & cols"], data["No fo rows & cols"])
    data["userBoard"] = emptyGrid(data["No fo rows & cols"], data["No fo rows & cols"])
    data["temporaryShip"] = []
    data["numUserShip"] = 0
    data["computerBoard"] = addShips(data["computerBoard"], data["numShips"])
    data["winner"] = None
    data["maxTurns"] = 10
    data["currentTurn"] = 0
    return


'''
makeView(data, userCanvas, compCanvas)
Parameters: dict mapping strs to values ; Tkinter canvas ; Tkinter canvas
Returns: None
'''
def makeView(data, userCanvas, compCanvas):
    drawGrid(data, userCanvas, data["userBoard"], True)
    drawGrid(data, compCanvas, data["computerBoard"], False)
    drawShip(data, userCanvas, data["temporaryShip"])
        # To display on both the canvas
    if data["winner"] == "user":
        drawGameOver(data, userCanvas)
    if data["winner"] == "comp":
        drawGameOver(data, compCanvas)
    if data["winner"] == "draw":
        drawGameOver(data, compCanvas)
        drawGameOver(data, userCanvas)
    return


'''
keyPressed(data, events)
Parameters: dict mapping strs to values ; key event object
Returns: None
'''
def keyPressed(data, event):
    if event.keysym == "Return":
        makeModel(data)
    pass


'''
mousePressed(data, event, board)
Parameters: dict mapping strs to values ; mouse event object ; 2D list of ints
Returns: None
'''
def mousePressed(data, event, board):
    coordinates = getClickedCell(data, event) #returns x,y coordinates
    row = coordinates[0]
    col = coordinates[1]

    if data["winner"] == None:
        if board == "user":
            clickUserBoard(data, row, col)

        if ((board == "comp") and (data["numUserShip"] == 5)):
            runGameTurn(data, row, col)


    pass

#### WEEK 1 ####

'''
emptyGrid(rows, cols)
Parameters: int ; int
Returns: 2D list of ints
'''
def emptyGrid(rows, cols):
    board = []
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(EMPTY_UNCLICKED)
        board.append(col)
    return board

'''
createShip()
Parameters: no parameters
Returns: 2D list of ints
'''
def createShip():
    ship = []
    row = random.randint(1, 8)
    col = random.randint(1, 8)
    axis = random.randint(0, 1)
    if axis == 0: #0 is vertical
        for i in range(row-1, row+2):
            ship.append([i, col])
    else:
        for i in range(col-1, col+2):
            ship.append([row, i])
    return ship

'''
checkShip(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def checkShip(grid, ship):
    for i in range(len(ship)):
        if grid[ship[i][0]][ship[i][1]] != EMPTY_UNCLICKED:
            return False
    return True

'''
addShips(grid, numShips)
Parameters: 2D list of ints ; int
Returns: 2D list of ints
'''
def addShips(grid, numShips):
    board = grid
    count = 0
    while count < numShips:
        ship = createShip()
        if checkShip(board, ship) == True:
            for i in range(len(ship)):
                board[ship[i][0]][ship[i][1]] = SHIP_UNCLICKED
            count += 1
    return board


'''
drawGrid(data, canvas, grid, showShips)
Parameters: dict mapping strs to values ; Tkinter canvas ; 2D list of ints ; bool
Returns: None
'''
def drawGrid(data, canvas, grid, showShips):
    for i in range(data["No fo rows & cols"]):
        for j in range(data["No fo rows & cols"]):
            x1 = data["cellsize"]*j
            y1 = data["cellsize"]*i
            x2 = data["cellsize"]+x1
            y2 = data["cellsize"]+y1
            fillColor = "#3F5E98"
            if showShips:
                if grid[i][j] == SHIP_UNCLICKED:
                    fillColor = "#FFDB15"
            if grid[i][j] == SHIP_CLICKED:
                fillColor = "#E4021B"
            if grid[i][j] == EMPTY_CLICKED:
                fillColor = "#F4F2EB"
            canvas.create_rectangle(x1, y1, x2, y2, width=1, fill=fillColor)
            canvas.create_oval(450, 450, 500, 500, width=1, fill="black")
            canvas.create_text(475, 468, text="TURN", font=("Helvetica", 7, "bold"), fill="white")
            canvas.create_text(475, 482, text=data["currentTurn"], font=("Helvetica", 10, "bold"), fill="white")



    return


### WEEK 2 ###

'''
isVertical(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isVertical(ship):
    for i in range(len(ship)):
        if ship[0][1] != ship[i][1]:
            return False

    seq = []
    for i in range(len(ship)):
        seq.append(ship[i][0])
    seq.sort()

    for i in range(len(ship)-1):
        if 1+seq[i] != seq[i+1]:
            return False
    return True

'''
isHorizontal(ship)
Parameters: 2D list of ints
Returns: bool
'''
def isHorizontal(ship):
    for i in range(len(ship)):
        if ship[0][0] != ship[i][0]:
            return False

    seq = []
    for i in range(len(ship)):
        seq.append(ship[i][1])
    seq.sort()

    for i in range(len(ship)-1):
        if 1+seq[i] != seq[i+1]:
            return False
    return True


'''
getClickedCell(data, event)
Parameters: dict mapping strs to values ; mouse event object
Returns: list of ints
'''
def getClickedCell(data, event):
    x = int(event.y/data["cellsize"])
    y = int(event.x/data["cellsize"])
    return [x, y]


'''
drawShip(data, canvas, ship)
Parameters: dict mapping strs to values ; Tkinter canvas; 2D list of ints
Returns: None
'''
def drawShip(data, canvas, ship):
    for i in range(len(ship)):
        x = ship[i][1]
        y = ship[i][0]
        x1 = data["cellsize"]*x
        y1 = data["cellsize"]*y
        x2 = data["cellsize"]+x1
        y2 = data["cellsize"]+y1
        canvas.create_rectangle(x1, y1, x2, y2, width=1, fill="#F4F2EB")
    return


'''
shipIsValid(grid, ship)
Parameters: 2D list of ints ; 2D list of ints
Returns: bool
'''
def shipIsValid(grid, ship):
    if len(ship) == 3:
        if checkShip(grid, ship):
            if isVertical(ship):
                return True
            elif isHorizontal(ship):
                return True
    return False


'''
placeShip(data)
Parameters: dict mapping strs to values
Returns: None
'''
def placeShip(data):
    if shipIsValid(data["userBoard"], data["temporaryShip"]):
        ship = data["temporaryShip"]
        board = data["userBoard"]
        for i in range(len(ship)):
            board[ship[i][0]][ship[i][1]] = SHIP_UNCLICKED
        data["numUserShip"] += 1
        data["temporaryShip"] = []
    else:
        data["temporaryShip"] = []
        print("Ship not in line")
    return


'''
clickUserBoard(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def clickUserBoard(data, row, col):
    userShip = data["temporaryShip"]
    userCoordinates = [row, col]
    numUserShip = data["numUserShip"]

    #check No of user ships
    if numUserShip == 5:
        return

    #check if user coordinates are already present in user ship
    for i in range(len(userShip)):
        if userCoordinates == userShip[i]:
            return
    userShip.append(userCoordinates)

    #check if user passed 3 coordinates for ship
    if len(userShip) == 3:
        placeShip(data) 
    #checking No of ships added
    if numUserShip == 5:
        print("Ships are ready to fire")

    return


### WEEK 3 ###

'''
updateBoard(data, board, row, col, player)
Parameters: dict mapping strs to values ; 2D list of ints ; int ; int ; str
Returns: None
'''
def updateBoard(data, board, row, col, player):
    if board[row][col] == SHIP_UNCLICKED:
        board[row][col] = SHIP_CLICKED
    elif board[row][col] == EMPTY_UNCLICKED:
        board[row][col] = EMPTY_CLICKED
    if isGameOver(board):
        data["winner"] = player
    return


'''
runGameTurn(data, row, col)
Parameters: dict mapping strs to values ; int ; int
Returns: None
'''
def runGameTurn(data, row, col):
    computerBoard = data["computerBoard"]
    userBoard = data["userBoard"]

    if ((computerBoard[row][col] == EMPTY_UNCLICKED) or (computerBoard[row][col] == SHIP_UNCLICKED)):
        updateBoard(data, computerBoard, row, col, "user")
        compCoordinaes = getComputerGuess(userBoard)
        updateBoard(data, userBoard, compCoordinaes[0], compCoordinaes[1], "comp")
        data["currentTurn"] += 1
        if data["currentTurn"] == data["maxTurns"]:
            data["winner"] = "draw"


    return


'''
getComputerGuess(board)
Parameters: 2D list of ints
Returns: list of ints
'''
def getComputerGuess(board):
    i = 0
    while i < 1:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if ((board[row][col] == EMPTY_UNCLICKED) or (board[row][col] == SHIP_UNCLICKED)):
            i += 1
            return [row, col]


'''
isGameOver(board)
Parameters: 2D list of ints
Returns: bool
'''
def isGameOver(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == SHIP_UNCLICKED:
                return False
    return True


'''
drawGameOver(data, canvas)
Parameters: dict mapping strs to values ; Tkinter canvas
Returns: None
'''
def drawGameOver(data, canvas):
    if data["winner"] == "user":
        canvas.create_rectangle(0, 120, 500, 340, width=1, fill="white")
        canvas.create_text(250, 180, text="Victory!!!", font=("Helvetica", 80, "bold"), fill="#104210")
        canvas.create_text(250, 250, text="You won against our AI", font=("Helvetica", 30, "bold"), fill="#0A0A00")
        canvas.create_text(250, 320, text="Press Enter to play again.", font=("Helvetica", 30, "bold"), fill="#050533")
    elif data["winner"] == "comp":
        canvas.create_rectangle(0, 120, 500, 340, width=1, fill="white")
        canvas.create_text(250, 180, text="Defeated!!!", font=("Helvetica", 60, "bold"), fill="#D01110")
        canvas.create_text(250, 250, text="You lost against our AI", font=("Helvetica", 30, "bold"), fill="#0A0A00")
        canvas.create_text(250, 320, text="Press Enter to play again.", font=("Helvetica", 30, "bold"), fill="#050533")
    elif data["winner"] == "draw":
        canvas.create_rectangle(0, 120, 500, 340, width=1, fill="white")
        canvas.create_text(250, 180, text="Draw!!!", font=("Helvetica", 80, "bold"), fill="#F6A21E")
        canvas.create_text(250, 250, text="You are out of moves", font=("Helvetica", 30, "bold"), fill="#0A0A00")
        canvas.create_text(250, 320, text="Press Enter to play again", font=("Helvetica", 30, "bold"), fill="#050533")
    return

### SIMULATION FRAMEWORK ###

from tkinter import *

def updateView(data, userCanvas, compCanvas):
    userCanvas.delete(ALL)
    compCanvas.delete(ALL)
    makeView(data, userCanvas, compCanvas)
    userCanvas.update()
    compCanvas.update()

def keyEventHandler(data, userCanvas, compCanvas, event):
    keyPressed(data, event)
    updateView(data, userCanvas, compCanvas)

def mouseEventHandler(data, userCanvas, compCanvas, event, board):
    mousePressed(data, event, board)
    updateView(data, userCanvas, compCanvas)

def runSimulation(w, h):
    data = {}
    makeModel(data)

    root = Tk()
    root.resizable(width=False, height=False) # prevents resizing window

    # We need two canvases - one for the user, one for the computer
    Label(root, text="USER BOARD - click cells to place ships on your board.").pack()
    userCanvas = Canvas(root, width=w, height=h)
    userCanvas.configure(bd=0, highlightthickness=0)
    userCanvas.pack()

    compWindow = Toplevel(root)
    compWindow.resizable(width=False, height=False) # prevents resizing window
    Label(compWindow, text="COMPUTER BOARD - click to make guesses.").pack()
    compCanvas = Canvas(compWindow, width=w, height=h)
    compCanvas.configure(bd=0, highlightthickness=0)
    compCanvas.pack()

    makeView(data, userCanvas, compCanvas)

    root.bind("<Key>", lambda event: keyEventHandler(data, userCanvas, compCanvas, event))
    compWindow.bind("<Key>", lambda event: keyEventHandler(data, userCanvas, compCanvas, event))
    userCanvas.bind("<Button-1>", lambda event: mouseEventHandler(data, userCanvas, compCanvas, event, "user"))
    compCanvas.bind("<Button-1>", lambda event: mouseEventHandler(data, userCanvas, compCanvas, event, "comp"))

    updateView(data, userCanvas, compCanvas)

    root.mainloop()


### RUN CODE ###

# This code runs the test cases to check your work
if __name__ == "__main__":
    ## Finally, run the simulation to test it manually ##
    runSimulation(500, 500)
