ass Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend < -2**31 or dividend > 2**31 - 1:
            return 2**31 - 1
        elif divisor == 1:
            return dividend
        elif divisor == -1:
            if -dividend > 2** 31 - 1:
                return 2**31 - 1
            return -dividend
        
        absdividend = abs(dividend)
        bindivisor = abs(divisor)
        result = 0
        if bindivisor > absdividend:
            return 0
        else:
            digit = 1
            while (bindivisor + bindivisor) <= absdividend:
                bindivisor += bindivisor
                digit += digit

        while digit > 0:
            if absdividend >= bindivisor:
                result += digit
                absdividend -= bindivisor
            bindivisor = bindivisor >> 1
            digit >>= 1
        
        if (dividend >= 0 and divisor < 0) or (dividend < 0 and divisor >= 0):
            result = -result
        
        if result < -2**31 or result > 2**31 - 1:
            return 2**31 - 1
        return result
