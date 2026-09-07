from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        visited = set()
        queue = deque()
        fresh = 0
        dirn = [(-1,0),(1,0),(0,-1),(0,1)]

        for r in range(R):
            for c in range(C):
                if(grid[r][c]==2):
                    queue.append((r,c))
                    visited.add((r,c))
                if(grid[r][c]==1):
                    fresh += 1
        
        count = 0
        minutes = 0
        while(queue):
            level_ran = len(queue)
            for _ in range(level_ran):
                r,c = queue.popleft()

                for ri,ci in dirn:
                    nw_r = r + ri
                    nw_c = c + ci

                    if(nw_r<0 or nw_r>=R or nw_c<0 or nw_c>=C or ((nw_r,nw_c) in visited) or grid[nw_r][nw_c]==0):
                        continue
                    #
                    fresh -= 1
                    visited.add((nw_r,nw_c))
                    queue.append((nw_r,nw_c))
            if(queue):
                minutes+=1
        
        
        return minutes if fresh==0 else -1
        