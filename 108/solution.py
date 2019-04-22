# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        n = len(nums)
        if n == 0:
            return None
        elif n == 1:
            return TreeNode(nums[0])
        
        result = TreeNode(nums[n/2])
        result.left = self.sortedArrayToBST(nums[:n/2])
        result.right = self.sortedArrayToBST(nums[n/2+1:])
        return result
