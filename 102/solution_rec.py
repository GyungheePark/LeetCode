# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []
        result = [[root.val]]
        l = self.levelOrder(root.left)
        r = self.levelOrder(root.right)
        n = len(l)
        m = len(r)
        if n <= m:
            for i in range(n):
                result.append(l[i]+r[i])
            for i in range(n, m):
                result.append(r[i])
        else:
            for i in range(m):
                result.append(l[i] + r[i])
            for i in range(m, n):
                result.append(l[i])
        return result

