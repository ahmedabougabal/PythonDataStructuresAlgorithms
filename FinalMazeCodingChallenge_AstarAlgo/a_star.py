from priority_queue import PriorityQueue

from helpers import offsets, create_maze, is_legal_pos, get_path

def heuristic(a, b): # this is what makes this algorithm more effecicent than Dijkstra algo
  x1,y1 = a
  x2, y2 = b
  return abs(x1 - x2) + abs(y1 - y2)


def print_maze_with_path(maze, path):
  for i in range(len(maze)):
    for j in range(len(maze[0])):
      if(i, j) in path:
        print("* ", end="")
      else:
        print(f"{maze[i][j]}", end= "")
    print()


#* g value is the cost from the start to current
def a_star(maze, start, goal):
  pq = PriorityQueue()
  predecessor = {start:None}
  g_values = {start: 0}
  pq.put(start,0)

  while not pq.is_empty():
    current = pq.get()
    if current == goal:
      return get_path(predecessor, start, goal)
    
    for direction in ["up", "right", "down", "left"]:
      x, y = offsets[direction]
      neighbour = (current[0] + x , current[1]+y)

      if is_legal_pos(maze, neighbour) and neighbour not in g_values:
        g_tentative = g_values[current] + 1
        g_values[neighbour] = g_tentative
        f_value = g_tentative + heuristic(goal, neighbour)
        pq.put(neighbour, f_value)
        predecessor[neighbour] = current

  return None


# testing 
if __name__ == "__main__":

  myMaze = create_maze();
    # Find and print path
  start = (0, 0)
  goal = (3, 3)
  path = a_star(myMaze, start, goal)
    
  if path:
    print("Path found!")
    print("Path coordinates:", path)
    print("\nMaze with path marked (*):")
    print_maze_with_path(myMaze, path)  # Fixed: Don't print the function itself
  else:
    print("No path found!")
  
