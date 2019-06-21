# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def aux(root):
            if root.left and root.right:
                (lendsnonroot, lendsroot) = aux(root.left)
                (rendsnonroot, rendsroot) = aux(root.right)
                endsnonroot = max(lendsnonroot, lendsroot, rendsnonroot, rendsroot, lendsroot + root.val + rendsroot)
                endsroot = max(root.val, lendsroot + root.val, rendsroot + root.val)
            elif root.left and not root.right:
                (lendsnonroot, lendsroot) = aux(root.left)
                endsnonroot = max(lendsnonroot, lendsroot)
                endsroot = max(root.val, lendsroot + root.val)
            elif not root.left and root.right:
                (rendsnonroot, rendsroot) = aux(root.right)
                endsnonroot = max(rendsnonroot, rendsroot)
                endsroot = max(root.val, rendsroot + root.val)
            else:
                endsnonroot = -2**31
                endsroot = root.val
            return (endsnonroot, endsroot)
        return max(aux(root))
