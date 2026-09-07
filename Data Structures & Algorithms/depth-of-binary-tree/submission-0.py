# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dep(root, maxi):
            if(root==None):
                return 0
            if(root.left==None and root.right==None):
                return maxi
            
            # recursive case
            left = dep(root.left, maxi+1)
            right = dep(root.right, maxi+1)
            return max(left, right)
        
        return dep(root, 1)
            