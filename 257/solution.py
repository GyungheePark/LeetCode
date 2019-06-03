# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        def aux(root, parents):
            result = []
            if root:
                if not parents:
                    cur = str(root.val)
                else:
                    cur = parents + "->" + str(root.val)
                if root.left and root.right:
                    result += aux(root.left, cur)
                    result += aux(root.right, cur)
                elif root.left and not root.right:
                    result += aux(root.left, cur)
                elif not root.left and root.right:
                    result += aux(root.right, cur)
                else:
                    result.append(cur)
            return result
        if not root:
            return []
        return aux(root, "")
