# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if(root==None):
                return (0, -float('inf'))
            
            left_curr, left_max = dfs(root.left)
            right_curr, right_max = dfs(root.right)

            left_curr = max(0, left_curr)
            right_curr = max(0, right_curr)

            curr_sum = root.val + max(left_curr, right_curr)
            # maxSum passes through node or benath it
            # vshape
            max_sum = max(root.val+left_curr+right_curr, left_max, right_max)

            return (curr_sum,max_sum)
        ans = dfs(root)
        return ans[1]