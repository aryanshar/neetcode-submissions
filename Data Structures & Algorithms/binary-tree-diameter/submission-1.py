# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Pair:
    def __init__(self):
        self.H = 0
        self.D = 0
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def DH(root):
            p = Pair()
            if(root==None):
                p.H = p.D = 0
                return p
            
            # otherwise
            left_p = DH(root.left)
            right_p = DH(root.right)

            p.H = max(left_p.H, right_p.H) + 1
            p.D = max(left_p.H+right_p.H , left_p.D, right_p.D)
            return p
        return DH(root).D
        