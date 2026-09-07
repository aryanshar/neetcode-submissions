# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        q = deque()

        if root==None:
            return []
        
        q.append(root)
        q.append(None)
        out = []
        while(len(q)):
            curr = q[0]
            q.popleft()
            if curr is not None:
                out.append(curr.val)
                left = curr.left
                if left:
                    q.append(left)
                right = curr.right
                if right:
                    q.append(right)
            else:
                # pop first and level is completed so push level output
                output.append(out)
                out = []
                if len(q)!=0:
                    q.append(None)
        return output
