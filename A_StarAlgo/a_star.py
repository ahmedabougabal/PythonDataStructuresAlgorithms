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
    pq =  PriorityQueue()
    pq.put(start, 0) # give the start position a priority of 0
    # f value in the initial cell should be equivalent to its h value, because the g value is 0 
    # (distance from start to start is zero) (highest priority) - no need to calculate the heruistic dist.
    predecessors = {start:None}
    g_values= {start:0}

    # algo's logic
    while not pq.is_empty():
        currentCell = pq.get()
        if currentCell == goal:
            return get_path(predecessors, start, goal)
        
        for direction in offsets.keys():
            rowOffset, colOffset = offsets[direction]
            neighbour = (currentCell[0] + rowOffset, currentCell[1] + colOffset) # that is the i-j coordinates  

            if is_legal_pos(maze, neighbour) and neighbour not in g_values: # (not in g_values == undiscovered)
                new_cost = g_values[currentCell] + 1 # as cells are connected by edges and the weight of each edge is 1  (we are not dealing with a weighted graph here)
                g_values[neighbour] = new_cost
                f_value = new_cost + heuristic(goal, neighbour)
                pq.put(neighbour, f_value)
                predecessors[neighbour] = currentCell

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
