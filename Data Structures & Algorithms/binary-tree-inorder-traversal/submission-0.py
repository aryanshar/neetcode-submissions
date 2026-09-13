# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.output = []
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if(root==None):
            return []
        self.inorderTraversal(root.left)
        self.output.append(root.val)
        self.inorderTraversal(root.right)

        return self.output
        
        