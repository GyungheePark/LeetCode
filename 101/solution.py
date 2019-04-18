# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def symmetric(l, r):
            if not l and not r:
                return True
            if not l and r:
                return False
            if l and not r:
                return False
            return(l.val == r.val and symmetric(l.right, r.left) and symmetric(l.left, r.right))
        
        if not root:
            return True
        return symmetric(root.left, root.right)


