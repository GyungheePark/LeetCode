class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        cur = 1
        carry = 0
        maxbit = 1 << 31
        result = 0
        while cur <= maxbit:
            abit = cur & a
            bbit = cur & b
            sumbit = abit ^ bbit ^ carry
            carry = ((abit and bbit) or  (bbit and carry) or (abit and carry)) << 1
            if sumbit:
                result = result | cur
            cur = cur << 1
        if result & maxbit:
            result = -(result ^ 0b11111111111111111111111111111111) - 1
        return result
