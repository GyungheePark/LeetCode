class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return matrix
        n = len(matrix)
        m = len(matrix[0])
        colmult = [1] * m
        rowmult = [1] * n
        
        for i in range(n):
            for j in range(m):
                colmult[j] *= matrix[i][j]
                rowmult[i] *= matrix[i][j]
        
        for i in range(n):
            for j in range(m):
                if colmult[j] == 0 or rowmult[i] == 0:
                    matrix[i][j] = 0
                               
