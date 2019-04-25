# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = deque()
        q = deque()
        q.append((root, 0))
        while q:
            node, i = q.popleft()
            if i == len(result):
                result.appendleft([node.val])
            else:
                result[len(result)-i-1].append(node.val)
            if node.left:
                q.append((node.left, i+1))
            if node.right:
                q.append((node.right, i+1))
        return result
