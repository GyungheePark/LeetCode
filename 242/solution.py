class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        occ = [0 for _ in range(26)]
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            occ[ord(s[i]) - 97] += 1
            occ[ord(t[i]) - 97] -= 1
        return all(v == 0 for v in occ)
