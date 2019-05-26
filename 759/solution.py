class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        n = len(S)
        dic = {}
        for i in range(n):
            if S[n-i-1] not in dic:
                dic[S[n-i-1]] = n-i-1
        
        result = []
        maxi = -1
        pre = -1
        for i in range(n):
            if maxi == -1:
                if dic[S[i]] != i:
                    maxi = dic[S[i]]
                else:
                    result.append(i - pre)
                    pre = i
            else:
                maxi = max(dic[S[i]], maxi)
                if i == maxi:
                    result.append(i - pre)
                    pre = i
                    maxi = -1
        return result
