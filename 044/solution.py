class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        def match(si, pi, s, p, memo):
            if memo[si][pi] == None:
                if pi == len(p):
                    memo[si][pi] = (si == len(s))
                elif si == len(s):
                    if p[pi] == "*":
                        memo[si][pi] = match(si, pi+1, s, p, memo)
                    else:
                        memo[si][pi] =  False
                elif p[pi] == "?":
                    memo[si][pi] = match(si+1, pi+1, s, p, memo)
                elif p[pi] == "*":
                    memo[si][pi] =  match(si+1, pi, s, p, memo) or match(si, pi+1, s, p, memo)
                else:
                    memo[si][pi] = (p[pi] == s[si]) and match(si+1, pi+1, s, p, memo)
            return memo[si][pi]

        memo = [[None for _ in range(len(p)+1)] for _ in range(len(s)+1)]
        return match(0, 0, s, p, memo)
