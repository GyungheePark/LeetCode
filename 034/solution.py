class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        l = len(nums)
        if l == 0:
            return [-1, -1]

        if l == 1:
            if nums[0] == target:
                return [0, 0]
            else:
                return [-1, -1]

        r1 = self.searchRange(nums[:l/2], target)
        r2 = self.searchRange(nums[l/2:], target)
        if r1 == [-1, -1] and r2 == [-1, -1]:
            return [-1, -1]
        elif r1 == [-1, -1] and r2 != [-1, -1]:
            return map(lambda x: x+l/2, r2)
        elif r1 != [-1, -1] and r2 == [-1, -1]:
            return r1
        else:
            return [r1[0], r2[1]+l/2]
