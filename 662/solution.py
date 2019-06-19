from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        q = deque()
        q.append((root, (0, 0)))
        result = 0
        dic = {}
        while q:
            node, (level, i) = q.popleft()
            if level not in dic:
                dic[level] = i
                result = max(result, 1)
            else:
                result = max(result, i - dic[level] + 1)
            if node.left:
                q.append((node.left, (level+1, 2*i)))
            if node.right:
                q.append((node.right, (level+1, 2*i+1)))
        return result
            
