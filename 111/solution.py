from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        q = deque()
        q.append((root, 1))
        while q:
            (node, d) = q.popleft()
            if not node.left and not node.right:
                return d
            if node.left:
                q.append((node.left, d+1))
            if node.right:
                q.append((node.right, d+1))
