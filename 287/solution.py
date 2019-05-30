class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        b = 0
        for n in nums:
            mask = 1 << (n-1)
            if b & mask != 0:
                return n
            b |= mask
