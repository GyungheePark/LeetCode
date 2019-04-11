class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        arr = [1 for _ in range(m)]
        for _ in range(n-1):
            for j in range(1, m):
                arr[j] += arr[j-1]
        return arr[m-1]
