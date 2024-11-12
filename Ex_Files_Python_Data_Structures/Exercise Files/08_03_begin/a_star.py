"""
Python Data Structures - A Game-Based Approach
A Star Algorithm maze solver.
Robin Andrews - https://compucademy.net/
Uses a priority queue containing f-values and (i, j) tuples along with dictionaries for
predecessors and g-values.
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from priority_queue import PriorityQueue


'''
#! some of my taken notes:

F = G + H , WHERE f here is the total cost 
G --> Cost from start to current node 
H --> estimated cost from current node to goal (heuristic)

Algo Implementation : 

Priority Queue: [(cell, F-value which is the total cost)] --> stores (position and f-score) tuples
G-scores dictionary - stores the value of blocks (cells) from start to current node 
H-scores : Manhattan distance to goals
predecessors dict : for path reconstruction
Get highest priority item from PQ (min F-Value): ....
Is it the goal?
If so, we are done
Otherwise:
put undiscovered neighbours,
calculate f-values
update predecessors
Repeat until queue is empty

'''

def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)


def a_star(maze, start, goal):
    pq = PriorityQueue()
    g_score = {}
    predecessors = {}

    # start position 
    g_score[start] = 0
    h_score = heuristic(start, goal)
    f_score = g_score[start] + h_score
    pq.put(start, f_score) # this is like the (item, priority)
    predecessors[start] = None

    while not pq.is_empty():
        # get the node with the lowest f score 
        current_pos  = pq.get() # since a pq has tuples of (priority , element) inside a list

        # check if we reached the goal
        if current_pos == goal:
            return get_path(predecessors, start, goal)
        
        # else , we explore the neighbours
        for direction in offsets.values():
            neighbour = (current_pos[0]+direction[0], current_pos[1] + direction[1])

            # skip the neighbour if it is blocked or invalid
            if not is_legal_pos(maze, neighbour):
                continue

            # calculate g score (cost from start to current node)
            g_value = g_score[current_pos] + 1

            # found better path to neighbour 
            if neighbour not in g_score or g_value < g_score[neighbour]:
                g_score[neighbour] = g_value
                h_score = heuristic(neighbour,goal)
                f_score = g_value + h_score

                # add to queue and update the predecessors
                pq.put(neighbour, f_score)
                predecessors[neighbour] = current_pos
    #No path is found
    return None




if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    # for row in maze:
    #     print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None
