class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if j == 0 or nums[j-1] != nums[j]:
                nums[i] = nums[j]
                i += 1
        return i
