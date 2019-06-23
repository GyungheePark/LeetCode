from collections import deque
class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return -1
        
        n = len(grid)
        visited = [[False for _ in range(n)] for _ in range(n)]
        q = deque()
        if grid[0][0] == 0:
            visited[0][0] = True
            q.append(((0, 0), 1))
        else:
            return -1
        adjs = [[0, 1], [1, 0], [0, -1], [-1, 0], [1, -1], [1, 1], [-1, -1], [-1, 1]]
        while q:
            (i, j), l = q.popleft()
            for adji, adjj in adjs:
                r = i + adji
                c = j + adjj
                if 0 <= r < n and 0 <= c < n:
                    if grid[r][c] == 0 and not visited[r][c]:
                        if r == n-1 and c == n-1:
                            return l+1
                        visited[r][c] = True
                        q.append(((r, c), l+1))
        return -1
