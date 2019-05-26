from collections import defaultdict
class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        dic = defaultdict(int)
        for x in T:
            dic[x] += 1
        result = ""
        char = set()
        for s in S:
            result += s * dic[s]
            char.add(s)
        for s in dic:
            if s not in char:
                result += s * dic[s]
        return result
