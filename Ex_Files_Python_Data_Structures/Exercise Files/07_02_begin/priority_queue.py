"""
Python Data Structures - A Game-Based Approach
Priority Queue Class based on heapq.
Robin Andrews - https://compucademy.net/
"""

import heapq


class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0

    def put(self, item, priority): # push item into a PQ
        heapq.heappush(self.elements, (priority, item))
        # lower priority numbers get up first

    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def __str__(self):
        return str(self.elements)


if __name__ == "__main__":
    pq = PriorityQueue()
    # print(pq)
    # print(pq.is_empty())
    pq.put("python", (2))
    pq.put("code", (1))
    pq.put("meow", (3))
    # print(pq.is_empty())
    
    print(pq)
    print(pq.get())
    print(pq)

