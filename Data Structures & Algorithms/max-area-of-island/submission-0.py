class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R = len(grid)
        C = len(grid[0])

        visited = set()
        def dfs(r, c, count):
            # base case
            if(r<0 or r>=R or c<0 or c>=C or ((r, c) in visited) or (grid[r][c]==0)):
                return 0
             
            visited.add((r, c))
            ct_left = dfs(r+1, c, count+1)
            ct_right = dfs(r-1, c, count+1)
            ct_top = dfs(r, c+1, count+1)
            ct_down = dfs(r, c-1, count+1)

            return ct_left + ct_right + ct_top + ct_down + 1
        max_area = 0
        for r in range(R):
            for c in range(C):
                if((r, c) not in visited and grid[r][c]==1):
                    count = dfs(r, c, 0)
                    max_area = max(count, max_area)
        

        return max_area