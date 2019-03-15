class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        if len(nums) < 3:
            return result

        nums.sort()
        
        for i in range(len(nums)-2):
            if i != 0 and nums[i] == nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                jval = nums[j]
                kval = nums[k]
                if s == 0:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < len(nums) and nums[j] == jval:
                        j += 1
                    k -= 1
                    while k >= 0 and nums[k] == kval:
                        k -= 1
                elif s < 0:
                    j += 1
                    while j < len(nums) and nums[j] == jval:
                        j += 1
                else:
                    k -= 1
                    while k >= 0 and nums[k] == kval:
                        k -= 1
        return result
