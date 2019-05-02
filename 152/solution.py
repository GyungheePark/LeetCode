class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        neg = [1] * len(nums)
        dp = [0] * len(nums)
        dp[0] = nums[0]
        neg[0] = min(nums[0], 0)
        
        for i in range(1, len(nums)):
            if nums[i] >= 0:
                dp[i] = max(dp[i-1] * nums[i], nums[i])
                if neg[i-1] < 0:
                    neg[i] = neg[i-1] * nums[i]
                else:
                    neg[i] = 0
            else:
                if neg[i-1] < 0:
                    dp[i] = neg[i-1] * nums[i]
                    neg[i] = min(nums[i], dp[i-1] * nums[i])
                else:
                    if nums[i-1] == 0:
                        dp[i] = nums[i]
                        neg[i] = min(nums[i], 0)
                    else:
                        dp[i] = max(nums[i], nums[i] * nums[i-1])
                        neg[i] = dp[i-1] * nums[i]
        return max(dp)
