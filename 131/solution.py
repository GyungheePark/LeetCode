from collections import deque
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        result = []
        result.append(list(s))
        q = deque()
        q.append(list(s))
        while q:
            l = q.popleft()
            n = len(l)
            for i in range(n):
                if i < n-1:
                    if l[i] == l[i+1]:
                        newl = l[:i]
                        newl.append(l[i]+l[i+1])
                        newl += l[i+2:]
                        q.append(newl)
                        if newl not in result:
                            result.append(newl)
                if i < n-2:
                    if l[i] == l[i+2]:
                        newl = l[:i]
                        newl.append(l[i] + l[i+1] + l[i+2])
                        newl += l[i+3:]
                        q.append(newl)
                        if newl not in result:
                            result.append(newl)
        return result
