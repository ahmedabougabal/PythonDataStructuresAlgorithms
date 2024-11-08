offsets = {
  "right" : (0,1),
  "left" : (0,-1),
  "up" : (-1,0),
  "down" : (1,0),
}

'''
this offset config works well too
offsets = {
  "up" : (-1,0),
  "down": (1,0),
  "left" : (0,-1),
  "right":(0,1)
}

'''

def create_maze():
    return [
        [" ", " ", "0", " "],
        [" ", " ", " ", " "],
        [" ", "0", " ", "0"],
        [" ", " ", " ", " "]
    ]

def is_legal_pos(maze, pos):
    i, j = pos
    nums_rows = len(maze)
    nums_cols = len(maze[0])
    return 0 <= i < nums_rows and 0 <= j < nums_cols and maze[i][j] != "0" and maze[i][j] != "*"


def get_path(predecessors, start, goal):
  currentCell = goal
  path = []
  while currentCell != start:
    path.append(currentCell)
    currentCell = predecessors[currentCell]
  path.append(start)
  path.reverse()
  return path
