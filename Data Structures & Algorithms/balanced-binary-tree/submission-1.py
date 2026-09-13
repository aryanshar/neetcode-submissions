# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def bal(root):
            if(root==None):
                return (True, 0)
            
            isbal_left, h_left = bal(root.left)
            isbal_right, h_right = bal(root.right)

            check_h_bal = abs(h_left-h_right)<=1
            bala = check_h_bal and isbal_left and isbal_right
            h = max(h_left, h_right) + 1

            return (bala, h)
        
        return bal(root)[0]