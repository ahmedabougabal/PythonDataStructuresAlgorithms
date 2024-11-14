offsets = {
  "up" : (-1,0),
  "down" : (1,0),
  "left" : (0,-1),
  "right" : (0,1)
}

def create_maze():
  return [
    [" ", " ", "0"," "],
    [" ", " ", " "," "],
    [" ", "0", " ","0"],
    [" ", " ", " "," "],
  ]

def is_legal_pos(maze, pos):
  x,y = pos
  x_rows= len(maze)
  y_cols = len(maze[0])
  return 0 <= x < x_rows and 0 <= y < y_cols and maze[x][y] != "0"


def get_path(predecessor, start, goal):
  currentCell = goal
  path =[]
  while currentCell != start:
    path.append(currentCell)
    currentCell = predecessor[currentCell]
  path.append(start)
  path.reverse()
  return path






