class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.root = root
        self.path = []
        self.var = 0
        self.treeTraversal(p.val)
        return self.treeTraversal(q.val, 2)

    def treeTraversal(self, target, traversalCount=1):
        currNode, prevNode = self.root, None
        while True:
            if traversalCount == 1:
                self.path.append(currNode.val)
            else:
                if self.path[self.var] == currNode.val:
                    self.var += 1
                else:
                    return prevNode #LCA

            if currNode.val != target:
                if currNode.val > target:
                    if currNode.left is not None:
                        prevNode = currNode
                        currNode = currNode.left
                    else:
                        break 
                elif currNode.val > target:
                    if currNode.right is not None:
                        prevNode = currNode
                        currNode = currNode.right
                    else:
                        break
            else:
                return currNode

from unittest import TestCase
class Tests(unittest.TestCase):
    def testcaseone(self):
        pass
    def testcasetwo(self):
        pass

if __name__=='__main__':
    unittest.main()