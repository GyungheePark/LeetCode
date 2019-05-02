class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxs = [0] * len(nums)
        mins = [0] * len(nums)
        maxs[0] = nums[0]
        mins[0] = nums[0]
        for i in range(1, len(nums)):
            maxs[i] = max(nums[i], maxs[i-1] * nums[i], mins[i-1] * nums[i])
            mins[i] = min(nums[i], maxs[i-1] * nums[i], mins[i-1] * nums[i])
        return max(maxs)
