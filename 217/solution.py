class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for n in nums:
            if n in seen:
                return True
            else:
                seen.add(n)
        return False
