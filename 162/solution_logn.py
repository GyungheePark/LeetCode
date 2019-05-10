class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        n = len(nums)
        if nums[n/2-1] < nums[n/2]:
            return n/2 + self.findPeakElement(nums[n/2:])
        else:
            return self.findPeakElement(nums[:n/2])
