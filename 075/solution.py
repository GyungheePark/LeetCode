ass Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            tmp = nums[i]
            j = i-1
            while j >= 0:
                if tmp < nums[j]:
                    nums[j+1] = nums[j]
                else:
                    break
                j -= 1
            nums[j+1] = tmp


