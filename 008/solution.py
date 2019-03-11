import itertools

class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MAX = 2**31 - 1
        INT_MIN = - 2**31
        words = str.split()
        result = 0
        if len(words):
            words = words[0]
            resultstr = ""
            if words[0] == '-':
                resultstr += "-"
                words = words[1:]
            elif words[0] == '+':
                words = words[1:]
            resultstr += "".join(itertools.takewhile(lambda x: x.isdigit(), words))
            
            if resultstr != "" and resultstr != "-":
                result = int(resultstr)
        
        if result < INT_MIN:
            result = INT_MIN
        elif result > INT_MAX:
            result = INT_MAX
        
        return result
