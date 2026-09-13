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
        def encode(root):
            if(root==None):
                output.append("N")
                return
            output.append(str(root.val))
            encode(root.left)
            encode(root.right)
            return output
        encode(root)
        return ",".join(output)

        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = list(data.split(","))
        self.i = 0
        def decode():
            val = data[self.i]
            self.i += 1
            if(val=="N"):
                return None
            root = TreeNode(val=int(val))
            root.left = decode()
            root.right = decode()
            return root
        
        return decode()


