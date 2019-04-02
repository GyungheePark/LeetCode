class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n/2+n%2):
            for j in range(n/2):
                tmp1 = matrix[j][n-1-i]
                matrix[j][n-1-i] = matrix[i][j]
                tmp2 = tmp1
                tmp1 = matrix[n-1-i][n-1-j]
                matrix[n-1-i][n-1-j] = tmp2
                tmp2 = tmp1
                tmp1 = matrix[n-1-j][i]
                matrix[n-1-j][i] = tmp2
                matrix[i][j] = tmp1
