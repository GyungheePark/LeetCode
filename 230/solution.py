# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        def aux(root, k):
            if not root:
                return (0, -1)
            ln, v = aux(root.left, k)
            if v != -1:
                return (ln, v)
            elif ln + 1 == k:
                return (ln, root.val)
            else:
                rn, v = aux(root.right, k - (ln + 1))
                if v != -1:
                    return (rn, v)
                else:
                    return (ln + rn + 1, -1)
                
        _, v = aux(root, k)
        return v
