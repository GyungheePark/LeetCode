# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def getHeight(root):
            if not root:
                return 0
            l = getHeight(root.left)
            r = getHeight(root.right)
            if l == -1 or r == -1:
                return -1
            if abs(l - r) <= 1:
                return 1 + max(l, r)
            else:
                return -1
            
        if not root:
            return True
        if getHeight(root) < 0:
            return False
        else:
            return True
