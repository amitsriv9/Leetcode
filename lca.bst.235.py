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
        self.modTraversal(root, p, False)
        res = self.modTraversal(root, q, True)
        return res
    
    # ensure all the inputs are non null
    def modTraversal(self, root, value, repeat=False):
        print(value)
        node = root
        previous = None
        indx = 0
        while True:
            if not repeat:
                self.path.append(node.val)
            else:
                print(self.path, indx, node.val)
                if len(self.path) <= indx:
                    break
                if self.path[indx] != node.val:
                    break
                else:
                    indx += 1
                    previous = node

            if node.val > value:
                if node.left:
                    node = node.left
                else:
                    print(f'match not found')
                    break

            elif node.val < value:
                if node.right:
                    node = node.right
                else:
                    print(f'match not found')
                    break
            
            else:
                print(f'match found {node.val} and  {value}')
                break
        return previous
    
    
from unittest import TestCase
class Tests(unittest.TestCase):
    def testcaseone(self):
        pass
    def testcasetwo(self):
        pass

if __name__=='__main__':
    unittest.main()