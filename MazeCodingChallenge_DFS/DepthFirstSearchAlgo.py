def create_maze():
    """creates a maze the same as in the image in the same directory as this file, 0 for open cells and 1 for
    blocked cells """
    return [
        [0, 0, 1, 0],
        [0, 0, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 0],
    ]


def is_valid_move(maze, visited, x, y):
    """checks if a move is valid (within bounds, not visited, not blocked)"""
    # check if position is within the maze bounds
    if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]):
        return False

    # checks if position is blocked or already visited
    if maze[x][y] == 1 or visited[x][y]:
        return False
    return True


def find_path(maze, start=(0, 0), end=(3, 3)):
    """finds the path from start to end using DFS"""
    rows = len(maze)
    cols = len(maze[0])
    # create a grid to keep track of visited cells
    visited = [[False for _ in range(cols)] for _ in range(rows)]

    # list to store the final path
    path = []

    def dfs(x, y):
        """recursive function for DFS"""
        visited[x][y] = True  # marks my current position as visited
        # if we reached the target, we found a path
        if (x, y) == end:
            path.append((x, y))
            return True

        # try all possible moves Right , Down , Left, Up
        moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for dx, dy in moves:
            next_x, next_y = x + dx, y + dy
            # checks if it is a valid move
            if is_valid_move(maze, visited, next_x, next_y):
                if dfs(next_x, next_y):
                    path.append((next_x, next_y))
                    return True
        return False

    # start dfs from starting position
    dfs(start[0], start[1])
    # reverse the path since we built in backwards
    return path[::-1]


# create and solve the maze
maze = create_maze()
print(maze)
path = find_path(maze)

print("path from (0, 0) to (3, 3) is \n >> ")
for x, y in path:
    print(f"{x}, {y}", end="--> " if (x, y) != path[-1] else "\n")

""" Course QUIZ
If you know a solution is not far
from the root of the tree:
>> BFS 

If the tree is very deep and
solutions are rare:
>> BFS (#!DFS WILL TAKE A LONG TIME GOING VERY VERY DEEP)

If the tree is very wide (not a binary tree):
>> DFS (#! BFS WILL NEED TOO MUCH MEMORY)

If solutions are frequent but
located deep in the tree:
>> DFS

determining whether a path exists
between two nodes:
>> DFS

Finding the shortest path:
>> BFS

conclusion : 
BFS is best for:
- Finding closest things
- Finding shortest paths
- When solution is likely nearby

DFS is best for: (uses less memory)
- Memory-efficient searching
- When solutions are deep
- When any solution will do

---------------------- Used DataStructure ----------------------
BFS (Queue):
- Takes from FRONT (pop(0))
- Adds to BACK (append)
- Like a line at a movie theater
- First person in line gets served first

DFS (Stack):
- Takes from TOP (pop())
- Adds to TOP (append)
- Like a stack of plates
- Last plate placed is first one taken
"""

# Depth First Search pseudocode
# Stack = [start_pos]
# predecessors : {start_pos, None}
"""
1-pop the stack 
2-is this the goal?
3-if so, exit , we are done.
4-otherwise, we push the undiscovered neighbours onto the stack and add them to predecessor/discovered list
predecessor meaning : when you move from one node to the next neighbouring node, the node you came from is called the 
predecessor of the current node.
"""
