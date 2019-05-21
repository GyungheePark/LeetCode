class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        cand1, cand2 = 0, 1
        count1, count2 = 0, 0
        for n in nums:
            if n == cand1:
                count1 += 1
            elif n == cand2:
                count2 += 1
            elif count1 == 0:
                cand1 = n
                count1 += 1
            elif count2 == 0:
                cand2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1
        result = []
        if nums.count(cand1) > len(nums)/3:
            result.append(cand1)
        if nums.count(cand2) > len(nums)/3:
            result.append(cand2)
        return result
