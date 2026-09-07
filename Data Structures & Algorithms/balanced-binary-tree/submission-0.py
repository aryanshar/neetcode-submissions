# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Pair:
    def __init__(self, h):
        self.H = h
        self.bal = True

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def balance(root):
            p = Pair(0)
            if(root==None):
                return p
            
            # otherwise check
            left = balance(root.left)
            right = balance(root.right)

            if(left.bal and right.bal and (abs(left.H-right.H) <=1)):
                p.H = max(left.H, right.H) + 1
                p.bal = True
                return p
            p.H = max(left.H, right.H) + 1
            p.bal = False
            return p
        return balance(root).bal

        