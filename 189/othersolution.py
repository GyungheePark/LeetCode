class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if k == 0:
            return
        
        def reverse(nums, lo, hi):
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1
        n = len(nums)
        k %= n
        reverse(nums, 0, n-k-1)
        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-1)
