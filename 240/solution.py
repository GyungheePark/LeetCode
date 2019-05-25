class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        def binsearch(matrix, j, hi, pivot):
            result = []
            rlo = 0
            rhi = hi
            if j < len(matrix):
                rlo = 0
                rhi = hi
                while rlo < rhi:
                    mid = (rlo + rhi) / 2
                    if matrix[j][mid] == pivot:
                        rlo = mid + 1
                        break
                    elif matrix[j][mid] > pivot:
                        rhi = mid
                    else:
                        rlo = mid + 1
                result.extend(matrix[j][rlo:hi])
            if j < len(matrix[0]):
                clo = 0
                chi = hi
                while clo < chi:
                    mid = (clo + chi) / 2
                    if matrix[mid][j] == pivot:
                        clo = mid + 1
                        break
                    elif matrix[mid][j] > pivot:
                        chi = mid
                    else:
                        clo = mid + 1
                result.extend([matrix[k][j] for k in range(clo,hi)])
            return result
        
        if not matrix or not matrix[0]:
            return False
        n = len(matrix)
        m = len(matrix[0])
        k = min(n,m)
        
        lo = 0
        hi = k
        while lo < hi:
            mid = (lo + hi)/2
            if target == matrix[mid][mid]:
                return True
            elif target < matrix[mid][mid]:
                hi = mid
            else:
                lo = mid + 1
        
        l = []
        pivot = matrix[lo-1][lo-1]
        result = [1]
        i = 0
        while result:
            result = binsearch(matrix, lo + i, lo, pivot)
            l.extend(result)
            i += 1
        if target in l:
            return True
        else:
            return False
