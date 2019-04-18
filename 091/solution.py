class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp = []
        for i in range(1, len(s)+1):
            if i == 1:
                if s[i-1] != '0':
                    dp.append(1)
                else:
                    dp.append(0)
            elif i == 2:
                if s[i-1] != '0':
                    n = dp[-1]
                else:
                    n = 0
                if s[i-2] != '0':
                    m = int(s[i-2:i])
                    if m >= 1 and m <= 26:
                        n += 1
                dp.append(n)
            else:
                if s[i-1] != '0':
                    n = dp[-1]
                else:
                    n = 0
                if s[i-2] != '0':
                    m = int(s[i-2:i])
                    if m >= 1 and m <= 26:
                        n += dp[-2]
                dp.append(n)
        return dp[-1]


