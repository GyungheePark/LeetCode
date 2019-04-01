class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) == 0:
            return []
        elif len(nums) == 1:
            return [nums]
        
        result = []
        for p in self.permute(nums[:-1]):
            for i in range(len(p) + 1):
                result.append(p[:i] + [nums[-1]] + p[i:])
        
        return result
        
