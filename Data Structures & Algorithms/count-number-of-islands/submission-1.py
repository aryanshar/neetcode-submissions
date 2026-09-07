# from collections import defaultdict
# class Graph():
#     def __init__(self, V):
#         self.V = V
#         self.graph = 

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        V = len(grid)
        R = len(grid)
        C = len(grid[0])
        visited = set()

        def dfs(r, c):
            # base case
            if(r<0 or r>=R or c<0 or c>=C or ((r, c) in visited) or (grid[r][c]=="0")):
                return
            visited.add((r, c))
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)

            # dfs only on 4 neighbours
            # for i in range(V):
            #     if(i not in visited and grid[node][i]!="0"):
            #         # call dfs
            #         dfs(i)
        count = 0
        for i in range(R):
            for j in range(C):
                if((i,j) not in visited and grid[i][j]!="0"):
                    dfs(i, j)
                    count += 1

        
        return count
        

        
        