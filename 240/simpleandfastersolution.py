class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix and matrix[0]:
            i = 0
            j = len(matrix[0]) - 1
            while i < len(matrix) and j >= 0:
                print matrix[i][j]
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] > target:
                    j -= 1
                else:
                    i += 1
        return False
