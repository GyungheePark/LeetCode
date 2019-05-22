import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k > len(nums)/2:
            heapq.heapify(nums)
            for i in range(len(nums)-k+1):
                n = heapq.heappop(nums)
        else:
            nums = [-n for n in nums]
            heapq.heapify(nums)
            for i in range(k):
                n = -heapq.heappop(nums)
        return n
