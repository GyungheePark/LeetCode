class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        k = m+n-1
        m -= 1
        n -=1
        while k >= 0:
            if m < 0:
                nums1[:k+1] = nums2[:n+1]
                break
            if n < 0:
                nums1[:k+1] = nums1[:m+1]
                break
            if nums1[m] <= nums2[n]:
                nums1[k] = nums2[n]
                k -= 1
                n -= 1
            else:
                nums1[k] = nums1[m]
                k -= 1
                m -= 1


