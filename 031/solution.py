class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        def helper(nums, j):
            if j == len(nums) or j == len(nums)-1:
                return False
            if j == len(nums) - 2:
                if nums[j+0] < nums[j+1]:
                    tmp = nums[j+0]
                    nums[j+0] = nums[j+1]
                    nums[j+1] = tmp
                    return True
                else:
                    return False
            if helper(nums, j+1):
                return True
            else:
                if j == 0 and nums[j+0] >= nums[j+1]:
                    nums.reverse()
                    return True
                elif nums[j+0] >= nums[j+1]:
                    return False
                tmp = nums[j+0]
                i = len(nums) - 1
                while i >= 0 and nums[i] <= tmp:
                    i -= 1
                nums[j+0] = nums[i]
                nums[i] = tmp
                nums[j+1:] = sorted(nums[j+1:])
                return True
        helper(nums, 0)
