class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        result = ""
        dic = {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"}
        digit = 1000
        while digit > 0:
            if num >= 9 * digit:
                result += (dic[digit] + dic[digit*10])
                num -= (digit * 9)
            elif num >= 5 * digit:
                result += dic[digit*5]
                num -= (digit * 5)
            if num >= 4 * digit:
                result += (dic[digit] + dic[digit*5])
                num -= (digit * 4)
            for i in range(num / digit):
                result += dic[digit]
            num %= digit
            digit /= 10
        return result
