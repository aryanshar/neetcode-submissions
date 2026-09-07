# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        out = []
        q = deque()
        if root==None:
            return []
        q.append(root)
        q.append(None)

        while(len(q)):
            curr = q[0]
            # pop the element
            q.popleft()
            if(curr==None):
                # level is done
                output.append(out)
                out = []
                if (len(q)):
                    q.append(None)
            else:
                left = curr.left
                right = curr.right
                out.append(curr.val)
                if(right):
                    q.append(right)
                if(left):
                    q.append(left)

        output = [x[0] for x in output]
        return output