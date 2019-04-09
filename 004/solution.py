class Solution(object):
    # Find index of the first element in nums that is greater than or equal to p
    # If all the elements are smaller than p, return -1
    def binarySearch(self, nums, p):
        n = len(nums)
        if n == 1:
            if nums[0] >= p:
                return 0
            else:
                return -1
        
        if p > nums[n/2]:
            i = self.binarySearch(nums[n/2:], p)
            if i == -1:
                return -1
            else:
                return n/2 + i
        else:
            i = self.binarySearch(nums[:n/2], p)
            if i == -1:
                return n/2
            else:
                return i
        
    def findIthSortedArrays(self, nums1, nums2, i):
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            return nums2[i]
        elif n == 0:
            return nums1[i]
        elif i == 0:
            return min(nums1[0], nums2[0])
        elif i == 1:
            if nums1[0] <= nums2[0]:
                if m > 1:
                    return min(nums1[1], nums2[0])
                else:
                    return nums2[0]
            else:
                if n > 1:
                    return min(nums1[0], nums2[1])
                else:
                    return nums1[0]
        elif m == 1 and nums1[0] <= nums2[0]:
            return self.findIthSortedArrays([], nums2, i-1)
        elif n == 1 and nums2[0] <= nums1[0]:
            return self.findIthSortedArrays(nums1, [], i-1)
        
        p = nums1[m/2]
        j = self.binarySearch(nums2, p)
        if j == -1:
            j = len(nums2)
        
        if i < j + m/2:
            return self.findIthSortedArrays(nums1[:m/2], nums2[:j], i)
        else:
            return self.findIthSortedArrays(nums1[m/2:], nums2[j:], i - (j + m/2))
        
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        if m == 0:
            if n % 2 == 0:
                return (float)(nums2[n/2-1] + nums2[n/2])/2.0
            else:
                return nums2[n/2]
        elif n == 0:
            if m % 2 == 0:
                return (float)(nums1[m/2-1] + nums1[m/2])/2.0
            else:
                return nums1[m/2]
        
        if (m+n) % 2 == 0:
            return (float)(self.findIthSortedArrays(nums1, nums2, (m+n)/2 - 1) + self.findIthSortedArrays(nums1, nums2, (m+n)/2))/2.0
        else:
            return self.findIthSortedArrays(nums1, nums2, (m+n)/2)
