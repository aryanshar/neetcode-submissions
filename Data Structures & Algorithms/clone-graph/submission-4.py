"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node==None:
            return None

        # visited = set()
        map_node = {}

        def dfs_clone(node):
            if node in map_node:
                return map_node[node]
            source = Node(node.val)
            map_node[node] = source
            for nbr in node.neighbors:
                cloned_nbr = dfs_clone(nbr)
                source.neighbors.append(cloned_nbr)
            return source
        return dfs_clone(node)