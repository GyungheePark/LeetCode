from collections import defaultdict
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = defaultdict(int)
        for n in nums:
            dic[n] += 1
            
        return map(lambda x: x[0], sorted(dic.items(), key = lambda x: x[1], reverse=True)[:k])
