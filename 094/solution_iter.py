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
        stack = [root]
        while stack:
            cur = stack.pop()
            if isinstance(cur, TreeNode):
                if cur.right != None:
                    stack.append(cur.right)
                stack.append(cur.val)
                if cur.left != None:
                    stack.append(cur.left)
            else:
                result.append(cur)
        return result
