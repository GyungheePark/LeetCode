class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            j = i+1
            while j < len(nums):
                if nums[i] + nums[j] == target:
                    return [i,j]
                else:
                    j += 1
