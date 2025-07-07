class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

from typing import Optional

class Solution:
    def __init__(self):
        self.leaf_nodes = {}  # key depth and value is list of node values at that depth
    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        deep_sum = 0
        if root:
            self.dfs(root)
            deep_sum = self.deep_leaf_sum()
        return deep_sum
    
    def deep_leaf_sum(self):
        _temp = max(self.leaf_nodes.keys())
        return sum(self.leaf_nodes[_temp])

    def dfs(self, root, depth=1):
        
        if root.left:
            self.dfs(root.left, depth+1)
        if root.right:
            self.dfs(root.right, depth+1)

        if root.left is None and root.right is None:
            maxdepth = max(self.leaf_nodes.keys() or [0])
            if depth >= maxdepth:
                if self.leaf_nodes.get(depth) is None:
                    self.leaf_nodes[depth] = [root.val]
                else:
                    self.leaf_nodes[depth].append(root.val)


import unittest
class Tests(unittest.TestCase):
    def tetscase_one(self):
        pass
if __name__=='__main__':
    unittest.main()