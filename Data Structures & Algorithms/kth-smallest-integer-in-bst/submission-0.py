# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res=None
        self.k = k
        def ans(root):
            if(root==None or self.res):
                return
            
            ans(root.left)
            self.k -= 1
            if(self.k==0):
                self.res = root.val
                return
            # otherwise process right
            ans(root.right)
        ans(root)
        return self.res
            
        