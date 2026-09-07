# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Pair:
    def __init__(self, val=TreeNode(), lca=False):
        self.val = val
        self.lca = lca
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def search(root, p):
            # searches if p subtree exists in root tree
            if(root==None and p==None):
                return True
            if(root==None and p!=None):
                return False
            if(root!=None and p==None):
                return False

            if(root==p):
                return True
            L = R = False
            if(root.left):
                L = search(root.left, p)
            if(root.right):
                R = search(root.right, p)
            return L or R
        
        def lca(root, p, q):
            pa = Pair()
            if(root==None):
                return pa
            
            left = lca(root.left, p, q)
            right = lca(root.right, p, q)

            # case: lca is in left or right subtree
            if left.lca or right.lca:
                pa.lca = True
                pa.val = left.val if left.lca else right.val
                return pa
            # case: lca passes thru root node
            l_p = search(root.left, p)
            r_p = search(root.right, p)
            l_q = search(root.left, q)
            r_q = search(root.right, q)
            if((l_q and r_p) or (l_p and r_q)):
                pa.lca=True
                pa.val = root
            elif(root==p and (l_q or r_q)):
                pa.lca=True
                pa.val=p
            elif(root==q and(l_p or r_p)):
                pa.lca=True
                pa.val=q
            else:
                pa.lca=False
            return pa
        
        pa = lca(root, p, q)
        return pa.val
            