import copy
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
        result = [[None for _ in matrix[0]] for _ in matrix]
        for i in xrange(n):
            for j in xrange(m):
                if matrix[i][j] == 0:
                    result[i][j] = 0
                    
        for i in xrange(n):
            for j in xrange(m):
                if result[i][j] != None:
                    if i < n-1:
                        if result[i+1][j] == None:
                            result[i+1][j] = result[i][j] + 1
                        else:
                            result[i+1][j] = min(result[i+1][j], result[i][j] + 1)
                    if j < m-1:
                        if result[i][j+1] == None:
                            result[i][j+1] = result[i][j] + 1
                        else:
                            result[i][j+1] = min(result[i][j+1], result[i][j] + 1)
        for i in xrange(n-1, -1, -1):
            for j in xrange(m-1, -1, -1):
                if result[i][j] != None:
                    if i > 0:
                        if result[i-1][j] == None:
                            result[i-1][j] = result[i][j] + 1
                        else:
                            result[i-1][j] = min(result[i-1][j], result[i][j] + 1)
                    if j > 0:
                        if result[i][j-1] == None:
                            result[i][j-1] = result[i][j] + 1
                        else:
                            result[i][j-1] = min(result[i][j-1], result[i][j] + 1)
        return result
