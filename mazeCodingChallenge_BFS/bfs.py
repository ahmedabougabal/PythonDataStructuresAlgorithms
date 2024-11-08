from helpers import get_path, is_legal_pos, offsets, create_maze
from queueClass import Queue # for BFS implementation

'''
find the shortest path between the starting pos and 
the goal cell
'''


def bfs(maze, start, goal):
  q = Queue()
  predecessors = {start:None}
  q.enqueue(start)
  while not q.is_empty():   
    cur = q.dequeue()
    if cur == goal:
      return get_path(predecessors, start, goal)
    for direction in offsets:
      row_offset, col_offset = offsets[direction]
      neighbour =  (cur[0] + row_offset, cur[1]+ col_offset) # add offset to the current position to calc the neighbouring position
      if is_legal_pos(maze, neighbour) and neighbour not in predecessors: 
        q.enqueue(neighbour)
        predecessors[neighbour] = cur
  return None 



if __name__ == "__main__":
    maze = create_maze()
    
    print("Maze Layout:")
    for row in maze:
        print(" ".join(row))
    
    start = (0, 0)
    goal = (3, 3)
    
    path = bfs(maze, start, goal)
    
    if path:
        print("\nPath found:", path)
    else:
        print("\nNo path found")

