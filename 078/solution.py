from collections import deque
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        q = deque()
        q.append(([], -1))
        while q:
            subset, i = q.popleft()
            result.append(subset)
            for j in range(i+1, len(nums)):
                newset = list(subset)
                newset.append(nums[j])
                q.append((newset, j))
        return result
