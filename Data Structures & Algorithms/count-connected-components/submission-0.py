from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        self.graph = defaultdict(list)
        # fill the graph
        for edge in edges:
            self.graph[edge[0]].append(edge[1])
            self.graph[edge[1]].append(edge[0])

        
        # graph is filled
        visited = set()

        def dfs(node):
            visited.add(node)
            for nbr in self.graph[node]:
                if(nbr not in visited):
                    dfs(nbr)
        
        count = 0
        for i in range(n):
            if(i not in visited):
                dfs(i)
                count += 1

        return count