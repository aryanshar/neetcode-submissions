from collections import defaultdict
class Graph():
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def check_in_item(self, u):
        if u not in self.graph.keys():
            return False
        return True
    def nbrs(self,u):
        return self.graph[u]
    def nodes(self):
        return self.graph.keys()

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        graph = Graph(n)

        for trus in trust:
            node = trus[0]
            nbr = trus[1]
            graph.add_edge(node, nbr)
        visited = set()
        def traverse(node):
            #base case
            # found
            if(node in graph.nodes()):
                return -1
            trust=0
            max_trust = 0
            for other in graph.nodes():
                if node in graph.nbrs(other):
                    trust += 1
            if(trust==n-1):
                return node
            return -1
        ans = -1
        for i in range(1,n+1):
            ans = max(ans,traverse(i))


        return ans
