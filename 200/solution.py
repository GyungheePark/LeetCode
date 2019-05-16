from collections import deque
class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def getAdjs(grid, i, j):
            adjs = []
            if i > 0 and grid[i-1][j] == "1":
                adjs.append((i-1, j))
            if i < len(grid)-1 and grid[i+1][j] == "1":
                adjs.append((i+1, j))
            if j > 0 and grid[i][j-1] == "1":
                adjs.append((i,j-1))
            if j < len(grid[0])-1 and grid[i][j+1] == "1":
                adjs.append((i, j+1))
            return adjs
        
        def dfs(grid, i, j):
            grid[i][j] = "0"
            for (ii, jj) in getAdjs(grid, i, j):
                dfs(grid, ii, jj)
                
        if not grid or not grid[0]:
            return 0
        
        n = len(grid)
        m = len(grid[0])
        
        island = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1":
                    island += 1
                    dfs(grid, i, j)
                    
        return island
