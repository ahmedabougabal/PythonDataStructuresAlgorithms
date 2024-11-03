"""
Python Data Structures A Game-Based Approach
Stack class
Robin Andrews https://compucademy.net/
"""


class Stack:
    def __init__(self):  # constructor gets called when we create an object
        self.items = []

    def is_empty(self):
        return self.items == []  # or return len(self.items) == 0
        # or return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]  # or return self.items[-1]

    def size(self):
        return len(self.items)  # return self.items.__len__()

    def __str__(self):  # this magic method defines how will your object should look like when you print it.
        # commenting this out will print the memory address where the object instantiated stored inside the memory
        # (memory Address)
        return str(self.items)


# : this line helps us control when we want to run the whole program versus when we just want to use parts of it
# somewhere else (when we import it somewhere else, only the methods for examples we use there will be executed
# without executing the whole main file here...
if __name__ == '__main__':
    s = Stack()
    print(s.is_empty())
    s.push(5)
    s.push(45)
    s.push(7)
    print(s.items)
    s.pop()
    print("after pop()")
    print(s.items)
    print(s.peek())  # 45
    print(s.pop())  # remove 45
    print(s.items)  # 5
