# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        if not root:
            return result
        if root.left != None:
            result += self.inorderTraversal(root.left)
        result.append(root.val)
        if root.right != None:
            result += self.inorderTraversal(root.right)
        return result 
