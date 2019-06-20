class Solution(object):
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        N = 0
        for i, s in enumerate(S):
            if s.isdigit():
                N *= int(s)
            else:
                N += 1
        
        for j in range(i, -1, -1):
            if S[j].isdigit():
                N /= int(S[j])
                K %= N
            else:
                if K == N or K == 0:
                    return S[j]
                else:
                    N -= 1
