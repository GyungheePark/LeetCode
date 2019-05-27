class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        v = 0
        for i in range(1, len(nums)+1):
            v ^= i
        for n in nums:
            v ^= n
        return v
