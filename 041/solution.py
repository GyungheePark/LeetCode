class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            cur = nums[i]
            while cur > 0 and cur <= len(nums) and nums[cur - 1] != cur:
                nextcur = nums[cur - 1]
                nums[cur - 1] = cur
                cur = nextcur
        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
        return len(nums) + 1
