class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        
        i = 0
        prev = self.countAndSay(n-1)
        result = ""
        while i < len(prev):
            cur = prev[i]
            curno = 1
            i += 1
            while i < len(prev) and cur == prev[i]:
                i += 1
                curno += 1
            result += (str(curno) + cur)
        return result
