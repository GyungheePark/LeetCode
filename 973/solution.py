class Solution(object):
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        lo = 0
        hi = len(A)
        while lo < hi:
            mid = (lo + hi)/2
            if A[mid] == 0:
                lo = mid
                break
            elif A[mid] < 0:
                lo = mid + 1
            else:
                hi = mid
        i = lo - 1
        j = lo
        result = []
        while True:
            if i >= 0 and j < len(A):
                if abs(A[i]) < abs(A[j]):
                    result.append(A[i]**2)
                    i -= 1
                elif abs(A[i]) > abs(A[j]):
                    result.append(A[j]**2)
                    j += 1
                else:
                    result.append(A[i]**2)
                    result.append(A[i]**2)
                    i -= 1
                    j += 1
            elif i < 0 and j < len(A):
                result.extend([x**2 for x in A[j:]])
                break
            elif i >= 0 and j >= len(A):
                for k in range(i+1):
                    result.append(A[i-k]**2)
                break
            else:
                break
        return result
