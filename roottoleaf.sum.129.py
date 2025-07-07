
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional
'''
visit all leaf nodes 
At leaf create numbers
finally add them  
'''
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.numbers = []
        if root:
            self.visit_leaves(root)
        return sum(self.numbers)
 
    def visit_leaves(self, root, val=0):
        if root.left:
            self.visit_leaves(root.left, 10*val + root.val)
    
        if root.right:
            self.visit_leaves(root.right, 10*val + root.val)
    
        if root.left is None and root.right is None:
            self.numbers.append(10*val+root.val)
            print(f'reached root at {root.val}')