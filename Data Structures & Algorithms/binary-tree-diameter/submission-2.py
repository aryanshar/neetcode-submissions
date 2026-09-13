# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        

        def diameter(root):
            if(root==None):
                return (0,0)
            left_d, left_h = diameter(root.left)
            right_d, right_h = diameter(root.right)

            h_max = max(right_h,left_h)+1
            d_max = max(left_d, right_d)

            return (max(d_max, right_h+left_h), h_max)
        
        return diameter(root)[0]