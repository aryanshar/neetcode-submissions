# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root1, root2):
            if(root1==None and root2==None):
                return True
            if((root1==None and root2!=None) or (root1!=None and root2==None)):
                return False
            
            left = isSame(root1.left, root2.left)
            right = isSame(root1.right, root2.right)

            if(left and right and root1.val==root2.val):
                return True
            
            return False
        
        def findTarget(root, subRoot):
            if(root==None and subRoot==None):
                return True
            if(root==None and subRoot!=None):
                return False
            if(root!=None and subRoot==None):
                return True
            
            if((root.val==subRoot.val)):
                # check Subtree
                if(isSame(root, subRoot)):
                    return True
            
            left = findTarget(root.left, subRoot)
            right = findTarget(root.right, subRoot)
            return left or right
        
        # def findTarget(root, subRoot):
        #     if(root==None and subRoot==None):
        #         return True
        #     if(root==None and subRoot!=None):
        #         return False
        #     if(root!=None and subRoot==None):
        #         return True
            
        #     # otherwise lets find all nodes where target is present and check isSame subt
        #     left = findTarget(root.left, subRoot)
        #     right = findTarget(root.right, subRoot)

        #     left_check = right_check = False

        #     if left:
        #         # target is in left
        #         left_check = isSame(root.left, subRoot)
        #     if right:
        #         # target can be in right
        #         right_check = isSame(root.right, subRoot)
        #     return left_check or right_check
        return findTarget(root, subRoot) 