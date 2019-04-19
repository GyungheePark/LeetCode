from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result = []
        q = deque([(root, 0)])
        while q:
            node, i = q.popleft()
            if node.left:
                q.append((node.left, i+1))
            if node.right:
                q.append((node.right, i+1))
            if i >= len(result):
                result.append(deque([node.val]))
            else:
                if i % 2 == 0:
                    result[i].append(node.val)
                else:
                    result[i].appendleft(node.val)
        return result
