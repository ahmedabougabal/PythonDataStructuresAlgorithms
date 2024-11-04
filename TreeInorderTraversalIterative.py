from typing import Optional, List
# could have used import Stack here but i wanted to use my own implementation while verifying my answer 
# on leetCode
class Stack:
    def __init__(self):  
        self.items = []

    def is_empty(self):
        return self.items == []  
        # or return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]  

    def size(self):
        return len(self.items)  

    def __str__(self):
        return str(self.items)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        res = []
        s = Stack()
        if not root:
            return []
        while cur or not s.is_empty(): # while either both are not null
            while cur:
                s.push(cur)
                cur = cur.left
            cur = s.pop() # node value which is stored in the stack will be popped out and added to res if there were no children 
            res.append(cur.val) 
            cur = cur.right
        return res
        
            
            
