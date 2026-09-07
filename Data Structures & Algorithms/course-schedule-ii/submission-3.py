from collections import defaultdict

class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def add_node(self, u, v):
        self.graph[u].append(v)
    


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        g = Graph(numCourses)
        def create_graph():
            for p in prerequisites:
                node = p[1]
                nbr = p[0]
                g.add_node(node, nbr)
        create_graph()
        
        # visited = set()
        # def dfs(node):
        #     visited.add(node)
        #     for nbr in g[node]:
        #         if(nbr not in visited):
        #             dfs(nbr)

        ## dfs code, returns false if cycle is found
        visited_new = set()
        parent = set()
        track = []
        def dfs_cycle(node, track, visited_new):
            if(node==None):
                return True
            visited_new.add(node)
            parent.add(node)
            for nbr in g.graph[node]:
                if(nbr not in visited_new):
                    check = dfs_cycle(nbr, track, visited_new)
                    if(check==False):
                        return False
                elif(nbr in parent):
                    return False
            track.append(node)
            parent.remove(node)
            return True
        
        for i in range(numCourses):
            check_dfs = dfs_cycle(i, track, visited_new)
            if(check_dfs==False):
                return []
        
        # find the node with the max neighbour/if clash find the one with min idx
        # trace its path
        trace = []
        visited = set()
        start = None
        max_size = 0
        for k, v in g.graph.items():
            if(len(v)>max_size):
                max_size = len(v)
                start = k

        dfs_cycle(start, trace, visited)
        for i in range(numCourses):
            if(i not in visited):
                trace.append(i)
        return trace[::-1]