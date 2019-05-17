class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        isPrime = [True for _ in range(n)]
        isPrime[0], isPrime[1] = False, False
        i = 2
        while i**2 < n:
            if i:
                j = i**2
                while j < n:
                    isPrime[j] = False
                    j += i
            i += 1
        cnt = 0
        for b in isPrime:
            if b:
                cnt += 1
        return cnt
