"""
Python Data Structures and Algorithms - A Game-Based Approach
Helper functions and values for use with other files in this project.
Robin Andrews - https://compucademy.net/
"""

offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


def read_maze(file_name):
    """
    Reads a maze stored in a text file and returns a 2d list containing the maze representation.
    """
    try:
        with open(file_name) as fh:
            maze = [[char for char in line.strip("\n")] for line in fh]
            num_cols_top_row = len(maze[0])
            for row in maze:
                if len(row) != num_cols_top_row:
                    print("The maze is not rectangular.")
                    raise SystemExit
            return maze
    except IOError:
        print("There is a problem with the file you have selected.")
        raise SystemExit


def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != "*"


def get_path(predecessors, start, goal): # used for backtracking the path from the goal to the start
    current = goal # start from the goal cell and then backtrack (work backwards)
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current] # predecessor is the 'parent' till current reaches start pos
    path.append(start)
    path.reverse() # reversing the list to get the right path
    return path


# adding tests
if __name__ == "__main__":
  file_path = "./mazes/challenge_maze.txt"
  maze = read_maze(file_path)
  print(maze)
