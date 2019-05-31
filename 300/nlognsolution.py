class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        S = []
        for n in nums:
            if not S:
                S.append(n)
            elif S[-1] < n:
                S.append(n)
            else:
                lo = 0
                hi = len(S)
                while lo < hi:
                    mid = (lo + hi) / 2
                    if S[mid] == n:
                        lo = mid
                        break
                    elif S[mid] > n:
                        hi = mid
                    else:
                        lo = mid + 1
                S[lo] = n
        return len(S)
