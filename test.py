from battleship import emptyGrid, addShips 
data = {}

data["rows"] = 10
data["cols"] = 10
data["boardSize"] = 500
data["cellWidth"] = data["boardSize"] / data["cols"]
data["cellHeight"] = data["boardSize"] / data["rows"]
data["numBoards"] = 2
data["numShips"] = 5
computerBoard = emptyGrid(data["rows"],data["cols"])
userBoard = emptyGrid(data["rows"],data["cols"])
computerBoard = addShips(computerBoard,data["numShips"])

values = data.values()
print(10 in values)