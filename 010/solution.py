class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == "":
            return s == ""
        
        if s == "" and len(p) >= 2 and p[1] == "*":
            return self.isMatch(s, p[2:])
        elif s != "":
            prevMatch = s[0] == p[0] or p[0] == "."
            if len(p) >= 2 and p[1] == "*":
                return self.isMatch(s, p[2:]) or (prevMatch and self.isMatch(s[1:], p))
            else:
                return prevMatch and self.isMatch(s[1:], p[1:])
        
        if s == "" and p == "":
            return True
        else:
            return False
