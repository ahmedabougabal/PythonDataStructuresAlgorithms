"""
Python Data Structures - A Game-Based Approach
Priority Queue Class based on heapq.
Robin Andrews - https://compucademy.net/
"""

import heapq

# min heap implementation (smaller numbers have higher priority)
class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority): # push item into a PQ
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1] # select the number to remove from the tuple
        # lower priority numbers are to be removed first (1 before 2 before 3)
    
    def __str__(self):
        return str(self.elements)


# lower numbers --> high priority task as in task scheduling (sys monitor)
if __name__ == "__main__":
    pq = PriorityQueue()
    # print(pq)
    # print(pq.is_empty())
    pq.put("python", (2))
    pq.put("code", (1))
    pq.put("meow", (3))
    # print(pq.is_empty())
    
    print(pq)
    print(pq.get()) # removed 'code' from pq
    print(pq)

