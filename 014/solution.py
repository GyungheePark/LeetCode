class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        result = ""
        if not len(strs):
            return result
        minlen = min(map(len, strs))
        for i in range(minlen):
            common = ""
            for j in range(len(strs)):
                if common == "":
                    common = strs[j][i]
                elif common != strs[j][i]:
                    common = ""
                    break;
            if common != "":
                if i == 0 or result != "":
                    result += common
        return result
        
