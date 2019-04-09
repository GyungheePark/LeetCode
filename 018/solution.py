class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = set()
        nums = sorted(nums)
        n = len(nums)
        for i in range(n-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if nums[i] + nums[n-3] + nums[n-2] + nums[n-1] < target:
                continue
            for j in range(i+1, n-2):
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break
                if nums[i] + nums[j] + nums[n-2] + nums[n-1] < target:
                    continue
                s, e = j+1, n-1
                while s < e:
                    v = nums[i] + nums[j] + nums[s] + nums[e]
                    if v == target:
                        result.add((nums[i], nums[j], nums[s], nums[e]))
                        s += 1
                        e -= 1
                    elif v < target:
                        s += 1
                    else:
                        e -= 1
        return result
