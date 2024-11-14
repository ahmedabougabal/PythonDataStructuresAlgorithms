#implementing a priority queue where it is a data structure where each element has a priority
import heapq

# elements with high priority (least f values) are served first

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def is_empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]
    
    def __str__(self):
        return str(self.elements)
    


# validating correctness of the priority queue
if __name__ == "__main__":
    pq = PriorityQueue()
    print("Empty queue:", pq)
    print("Is empty?", pq.is_empty())
    
    pq.put("eat", 2)
    pq.put("code", 1)
    pq.put("sleep", 3)
    
    print("After adding items:", pq)
    
    # Get items (should come out in priority order)
    print("First item:", pq.get())         
    print("Second item:", pq.get())        
    print("Third item:", pq.get())         