class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])
        memo = [[0 for _ in range(m)] for _ in range(n)]
        blocked = False
        for i in range(n):
            if not blocked:
                if obstacleGrid[i][0] != 1:
                    memo[i][0] = 1
                else:
                    blocked = True
                    memo[i][0] = 0
            else:
                memo[i][0] = 0
        blocked = False
        for j in range(m):
            if not blocked:
                if obstacleGrid[0][j] != 1:
                    memo[0][j] = 1
                else:
                    blocked = True
                    memo[0][j] = 0
            else:
                memo[0][j] = 0
        
        for i in range(1, n):
            for j in range(1, m):
                if obstacleGrid[i][j] == 1:
                    memo[i][j] = 0
                else:
                    memo[i][j] = memo[i-1][j] + memo[i][j-1]
        return memo[n-1][m-1]
                
