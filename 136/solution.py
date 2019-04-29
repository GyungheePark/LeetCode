class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)-1):
            nums[i+1] ^= nums[i]
        return nums[-1]
