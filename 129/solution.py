# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helper(node, v):
            nodev = v * 10 + node.val
            result = 0
            if node.left and node.right:
                result += helper(node.left, nodev) + helper(node.right, nodev)
            elif node.left:
                result += helper(node.left, nodev)
            elif node.right:
                result += helper(node.right, nodev)
            else:
                result += nodev
            return result
            
        if not root:
            return 0
        return helper(root, 0)
