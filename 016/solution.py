class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        n = len(nums)
        result = sum(nums[:3])
        for i in range(n-2):
            j = i+1
            k = n-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(s - target) < abs(result - target):
                    result = s
                if s < target:
                    j += 1
                elif s == target:
                    return s
                else:
                    k -= 1
        return result
