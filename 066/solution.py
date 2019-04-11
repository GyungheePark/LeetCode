class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        n = len(digits)
        for i in range(n):
            if digits[n-1-i] + 1 < 10:
                digits[n-1-i] += 1
                break
            else:
                digits[n-1-i] = 0
            if i == n-1:
                digits = [1] + digits
        return digits
