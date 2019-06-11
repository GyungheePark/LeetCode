class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        fst = 2 ** 31
        snd = 2 ** 31
        for n in nums:
            if n <= fst:
                fst = n
            elif n <= snd:
                snd = n
            else:
                return True
        return False
