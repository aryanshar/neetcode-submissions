# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if(root==None):
            return root
        if(root.left==None and root.right==None):
            return root
        
        # recursive
        left = root.left
        right = root.right
        # recursive call
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        root.left = right
        root.right = left

        return root



        d = invertTree(TreeNode())
        