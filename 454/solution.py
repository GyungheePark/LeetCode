from collections import defaultdict
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dic = defaultdict(int)
        for a in A:
            for b in B:
                dic[a+b] += 1

        result = 0
        for c in C:
            for d in D:
                if -c-d in dic:
                    result += dic[-c-d]
        return result
        
