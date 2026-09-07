# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # recurse in post-Order and 
        if(p==None and q==None):
            return True
        if(p==None and q is not None):
            return False
        if(p is not None and q==None):
            return False
        # otherwise
        left = self.isSameTree(p.left, q.left)
        right = self.isSameTree(p.right, q.right)

        if(left and right and p.val==q.val):
            return True
        
        return False
        