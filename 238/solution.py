class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        L = [1] * n
        R = [1] * n
        for i in range(1, n):
            L[i] = L[i-1] * nums[i-1]
            R[n-i-1] = R[n-i] * nums[n-i]
        return [L[i]*R[i] for i in range(len(nums))]
