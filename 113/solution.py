from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []
        if not root.left and not root.right:
            if root.val == sum:
                result.append(deque([root.val]))
            return result
        
        if root.left:
            for sub in self.pathSum(root.left, sum - root.val):
                sub.appendleft(root.val)
                result.append(sub)
        if root.right:
            for sub in self.pathSum(root.right, sum - root.val):
                sub.appendleft(root.val)
                result.append(sub)
        
        return result
