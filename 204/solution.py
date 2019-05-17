class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes = []
        for i in range(2, n):
            divisible = False
            for p in primes:
                if p**2 > i:
                    break
                if i % p == 0:
                    divisible = True
                    break
            if not divisible:
                primes.append(i)
        return len(primes)
        
