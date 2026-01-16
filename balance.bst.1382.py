class Solution:
    def __init__(self):
        self.height = {}
        self.height['left'] = [0]
        self.height['right'] = [0]

    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root:
            # while True
            self.check_height(root)
            left_is = max(self.height['left']) 
            right_is = max(self.height['right'])
            
            if left_is > right_is:
                print(f'left {left_is} side is greater. {right_is}')
                if left_is >= 2 + right_is:
                    root = self.right_rotation(root)
                 
            
            else:
                print(f'right {right_is} side is greater. {left_is}')
                if left_is + 2 <= right_is:
                    root = self.left_rotation(root)

        return root

    def check_height(self, root, height=1, subtree=''):
        if root.left:
            self.check_height(root.left, height+1, 'left' if height ==1 else subtree)

        if root.right:
            self.check_height(root.right, height+1, 'right' if height ==1 else subtree)
        
        if root.left is None and root.right is None:
            print("found leaf node")
            self.height[subtree].append(height)
    
    def right_rotation(self, root):
        print("right rotation")
        if root.left:
            new_root = root.left
            temp = new_root.right if new_root.right else None
            new_root.right = root
            root.left = temp
            return new_root

    def left_rotation(self, root):
        print("left rotation")
        if root.right:
            new_root = root.right
            temp = new_root.left if new_root.left else None
            new_root.left = root
            root.right = temp
            return new_root