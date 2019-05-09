class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return 0
        
        n = len(nums)
        i = self.findPeakElement(nums[:n/2])
        j = self.findPeakElement(nums[n/2:])
        if i == n/2-1:
            if nums[i] < nums[n/2]:
                return n/2 + j
            else:
                return i
        else:
            return i
