from typing import Optional, List

"""
pseudoCode
start at the root of a binary tree
traverse the left subtree
empty? backtrack to the root and add its value to the stack []
we will run the same steps recursively 

"""


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []  # this is where we store the node values and has nothing to do with the actual stack of the DFS Algorithm

        # the stack is actually
        # managed by Python's call stack during recursion

        # this is the recursive approach
        def inorder(root):
            if not root:
                return
            # if there is a root, traverse the tree
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        inorder(root)  # start the traversal from the root
        return res
