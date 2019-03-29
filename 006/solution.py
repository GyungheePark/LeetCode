class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        srows = [""] * numRows
        for j in range(len(s)):
            if j % ((numRows-1)*2) > numRows - 1:
                srows[numRows - 1 - (j % ((numRows-1)*2)) % (numRows-1)] += s[j]
            else:
                srows[j % ((numRows-1)*2)] += s[j]
        return "".join(srows)
