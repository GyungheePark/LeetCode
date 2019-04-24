class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        if not s:
            return True
        i = 0
        j = len(s) - 1
        while i < j:
            if not s[i].isalnum():
                i += 1
            else:
                if not s[j].isalnum():
                    j -= 1
                else:
                    if s[i].lower() == s[j].lower():
                        i += 1
                        j -= 1
                    else:
                        return False
        return True
