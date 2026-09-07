from collections import defaultdict




class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def add_node(self, u, v):
        self.graph[u].append(v)
    


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        # read second element first and first element is neighbor in pre-req
        # construct the graph
        # now count the elements, if cycle detected, then false
        # if total count>=numCourses on dfs, then true
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
        def dfs_cycle(node):
            if(node==None):
                return True
            visited_new.add(node)
            parent.add(node)
            for nbr in g.graph[node]:
                if(nbr not in visited_new):
                    check = dfs_cycle(nbr)
                    if(check==False):
                        return False
                elif(nbr in parent):
                    return False
            parent.remove(node)
            return True

        for i in range(numCourses):
            check_dfs = dfs_cycle(i)
            if(check_dfs==False):
                return False
        if(len(visited_new)==numCourses):
            return True
        return False
                

        