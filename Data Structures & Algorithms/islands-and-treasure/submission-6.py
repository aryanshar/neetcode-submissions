from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R = len(grid)
        C = len(grid[0])
        visited = set()
        queue = deque()

        for r in range(R):
            for c in range(C):
                if(grid[r][c]==0):
                    visited.add((r,c))
                    queue.append((r,c))
        dirn = [(-1,0),(1,0),(0,-1),(0,1)]
        # now our queue has starting positions for bfs from
        while(queue):
            r,c = queue.popleft()

            # now we have 4 directions to go
            for r_d,c_d in dirn:
                rn = r+r_d
                cn = c+c_d

                # this is the new neighbor
                # have certain conditions to visit this
                # we need to update grid results with length from source
                if(rn<0 or rn>=R or cn<0 or cn>=C or ((rn,cn) in visited) or grid[rn][cn]==-1):
                    continue
                grid[rn][cn] = 1 + grid[r][c]
                # mark as visited
                visited.add((rn,cn))
                queue.append((rn,cn))
        
#         def dfs(r, c):
#             # base case
#             if(r<0 or r>=R or c<0 or c>=C or ((r,c) in visited) or grid[r][c]==-1):
#                 return 2147483647
#             # case 1: grid[i][j] = 0 //treasure is found
#             elif(grid[r][c]==0):
#                 return 0
            
#             visited.add((r,c))

#             left = dfs(r, c-1)
#             right = dfs(r, c+1)
#             top = dfs(r-1, c)
#             bot = dfs(r+1, c)

#             new_num = 1+min((min(left,right),min(top,bot)))
#             grid[r][c] = min(grid[r][c],new_num)
#             visited.remove((r,c))
#             return new_num


#         for r in range(R):
#             for c in range(C):
#                 if((r,c) not in visited):
#                     dfs(r,c)