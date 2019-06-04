from collections import deque
class Solution(object):
    def updateMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]:
            return matrix
        n = len(matrix)
        m = len(matrix[0])
        
        result = [[2**31 for _ in range(m)] for _ in range(n)]
        q = deque()
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                    q.append((i,j))
        
        adjs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            (i, j) = q.popleft()
            for ii, jj in adjs:
                r, c = i + ii, j + jj
                if 0 <= r < n and 0 <= c < m and result[r][c] > result[i][j] + 1:
                    result[r][c] = result[i][j] + 1
                    q.append((r,c))
        return result
