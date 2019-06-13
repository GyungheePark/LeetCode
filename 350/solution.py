class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        nums1.sort()
        nums2.sort()
        i = 0
        result = []
        while i < len(nums1):
            cnt1 = 1
            cur = nums1[i]
            while i+1 < len(nums1) and nums1[i+1] == cur:
                i += 1
                cnt1 += 1
            # binary search on nums2
            lo = 0
            hi = len(nums2)
            while lo < hi:
                mid = (lo + hi)/2
                if nums2[mid] < cur:
                    lo = mid+1
                elif nums2[mid] > cur:
                    hi = mid
                else:
                    hi = mid
            if lo < len(nums2) and nums2[lo] == cur:
                cnt2 = 1
                while lo+1 < len(nums2) and nums2[lo+1] == cur:
                    lo += 1
                    cnt2 += 1
                result += [cur]*min(cnt1, cnt2)
            i += 1
        return result
        
