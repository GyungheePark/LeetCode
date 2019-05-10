class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator * denominator >= 0:
            pos = True
        else:
            pos = False
        numerator = abs(numerator)
        denominator = abs(denominator)
        result = ""
        if not pos:
            result += "-"
        result += str(numerator / denominator)
        if numerator % denominator == 0:
            return result
        else:
            result += "."
            numerator -= (numerator / denominator * denominator)
        rep = {}
        i = 0
        while numerator % denominator != 0:
            numerator *= 10
            if numerator in rep:
                i = rep[numerator]
                index = result.index('.') + i
                result = result[:index+1] + '(' + result[index+1:] + ')'
                return result
            else:
                result += str(numerator / denominator)
                rep[numerator] = i
                i += 1
                numerator -= (numerator / denominator * denominator)
        return result
