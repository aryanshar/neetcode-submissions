# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Pair:
    def __init__(self, mini=-1000000000, maxi=1000000000, bst=True):
        self.mini = mini
        self.maxi = maxi
        self.bst = bst

class Solution:

    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(root):
            p = Pair()
            # gives boolean and range of numbers in BST
            if(root==None):
                return p
            
            p_left = valid(root.left)
            p_right = valid(root.right)

            if(p_left.bst and p_right.bst):
                bool_left = True
                bool_right = True
                if(root.left):
                    # check range
                    bool_left = root.val>p_left.maxi
                    p.mini = p_left.mini
                else:
                    p.mini = root.val
                    
                if(root.right):
                    # check range
                    bool_right = root.val<p_right.mini
                    p.maxi = p_right.maxi
                else:
                    p.maxi = root.val

                p.bst = bool_left and bool_right    
            
            else:
                p.bst = False
            return p
        return valid(root).bst
        
        