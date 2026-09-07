from collections import defaultdict

class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def __call__(self):
        return self.graph

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        self.graph = Graph(n)

        for edge in edges:
            node = edge[0]
            nbr = edge[1]
            self.graph()[node].append(nbr)
            self.graph()[nbr].append(node)
        
        visited = set()

        def check_cycle(node, parent):
            visited.add(node)
            
            for nbr in self.graph()[node]:
                if(nbr not in visited):
                    check_nbr = check_cycle(nbr, node)
                    if(check_nbr==False):
                        return False

                elif(nbr!=parent):
                    return False
                
            return True
        check_tree = check_cycle(0, -1)
        if(len(visited)==n) and check_tree:
            return True
        return False


        