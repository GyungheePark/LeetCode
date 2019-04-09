class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        reach = nums[0]
        for i in range(1, n):
            if reach < i:
                return False
            if reach < i + nums[i]:
                reach = i + nums[i]
            if reach >= n-1:
                return True
        return True
