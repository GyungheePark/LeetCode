from fractions import gcd
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        n = len(nums)
        g = gcd(n,k)
        l = n * k / g
        for i in range(g):
            tmp = nums[((l/k - 1) * k + i)%n]
            for j in range(l/k):
                tmp2 = nums[(j*k+i)%n]
                nums[(j*k+i)%n] = tmp
                tmp = tmp2
        
