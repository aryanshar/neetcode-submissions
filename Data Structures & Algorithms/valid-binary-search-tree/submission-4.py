# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isbst(root, low, high):
            if(root==None):
                return True
            left = isbst(root.left, low, root.val)
            right = isbst(root.right, root.val, high)
            check_root = low < root.val < high
            return check_root and left and right
        
        return isbst(root, -float('inf'), float('inf'))