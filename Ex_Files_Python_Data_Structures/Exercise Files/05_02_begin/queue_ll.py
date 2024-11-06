from collections import deque # why have we used a deque 'doubly ended queue', instead of a list?
'''
a deque is more optimized to be used instead of a list as deletions and insertions at the begining will be 
quiet slow for larger datasets, so using a deque is a bit more optimized to handle the method implementations
in creating my own implementation for the queue. O(1) operations at both ends
'''

# file name has a double 'l' at the end to not override the existing built-in queue module
class Queue: # first in - first out 
    def __init__(self) -> None:
        self.items = deque()

    def is_empty(self):
        return len(self.items) == 0
        # return not self.items()
    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty(): # if the queue isnot empty
            return self.items.popleft()
        raise IndexError("Queue is Empty...")
    
    def size(self):
        return len(self.items)
    
    def peek(self):
        return self.items[0] 
        # return self.items.index(0) # this line searches for the value '0' and returns it's position
    
    def displayQueueItems(self):
        print(f"items count = {self.size()}, Items : ", end=" ")
        for i in range(len(self.items)):
            print(self.items[i], end=" ")
        print('')

    def __str__(self):
        return str(self.items)
        

if __name__ == "__main__":
    q = Queue()
    print(q)
    print(q.is_empty())
    q.enqueue(45)
    q.enqueue(33)
    q.enqueue(12)
    q.enqueue(63)
    q.enqueue(2)
    q.enqueue(6)
    print(q.peek()) # 45
    q.dequeue()
    print(q.peek()) # 33
    print(q.size()) # 5
    print(q.is_empty()) # false
    q.enqueue(4)
    print(q.size()) # 6
    print(q.dequeue()) # pops out the element and prints it
    q.displayQueueItems()
    print(q.peek()) 
    print(q)


