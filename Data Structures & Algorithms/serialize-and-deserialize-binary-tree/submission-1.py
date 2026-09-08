# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        output = []
        def dfs(root):
            if(root==None):
                output.append("N")
                return
            output.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ",".join(output)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(",")
        self.i = 0
        def construct_preorder():
            val = data[self.i]
            # data is read
            self.i += 1
            if(val=="N"):
                return None
            node = TreeNode(int(val))
            node.left = construct_preorder()
            node.right = construct_preorder()
            return node
        
        return construct_preorder()
