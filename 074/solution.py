class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        lo = 0
        hi = len(matrix)
        while lo < hi:
            mid = (lo + hi) / 2
            if matrix[mid][0] < target:
                lo = mid + 1
            elif matrix[mid][0] == target:
                return True
            else:
                hi = mid
        if lo < len(matrix) and matrix[lo][0] > target and lo == 0:
            return False
        lo -= 1
        clo = 0
        chi = len(matrix[lo])
        while clo < chi:
            mid = (clo + chi) / 2
            if matrix[lo][mid] < target:
                clo = mid + 1
            elif matrix[lo][mid] == target:
                return True
            else:
                chi = mid
        return False
