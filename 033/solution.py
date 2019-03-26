class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        elif len(nums) == 1:
            if nums[0] == target:
                return 0
            else:
                return -1
        
        # sorted nums and target out of range
        if nums[0] < nums[-1] and (target < nums[0] or target > nums[-1]):
            return -1
        
        length = len(nums)
        i1 = self.search(nums[:length/2], target)
        i2 = self.search(nums[length/2:], target)
        if i1 == -1 and i2 == -1:
            return -1
        elif i1 != -1 and i2 == -1:
            return i1
        elif i1 == -1 and i2 != -1:
            return length/2 + i2
        else:
            # UNREACHED
            return -1
