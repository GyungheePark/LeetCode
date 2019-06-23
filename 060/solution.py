class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        fac = [0, 1]
        for i in range(2, n+1):
            fac.append(fac[-1] * (i))

        result = []
        def aux(nums, n, k):
            if n == 1:
                result.append(str(nums[0]))
                return
            q = k / fac[n-1]
            result.append(str(nums[q]))
            k %= fac[n-1]
            nums = nums[:q] + nums[q+1:]
            aux(nums, n-1, k)
            
        nums = range(1, n+1)
        aux(nums, n, k-1)
        return "".join(result)
