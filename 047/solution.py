from collections import deque
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        if len(nums) == 1:
            return [deque([nums[0]])]
        
        result = []
        numset = set()
        for i in range(len(nums)):
            n = nums[i]
            if n not in numset:
                numset.add(n)
                for p in self.permuteUnique(nums[:i] + nums[i+1:]):
                    p.appendleft(n)
                    result.append(p)
                        
        return result
