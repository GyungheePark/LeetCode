class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def jumpto(nums, target):
            for i in range(target):
                if i + nums[i] >= target:
                    return i
        n = len(nums)
        if nums == [1] * n:
            return n-1
        target = n-1
        result = 0
        while target > 0:
            target = jumpto(nums, target)
            result += 1
        return result
