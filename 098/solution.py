# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        
        def helper(root):
            if root.left == None and root.right == None:
                return (root.val, root.val)
            elif root.left == None and root.right != None:
                minv, maxv = helper(root.right)
                if minv != -1 and root.val < minv:
                    return (root.val, maxv)
                else:
                    return (None, None)
            elif root.left != None and root.right == None:
                minv, maxv = helper(root.left)
                if maxv != None and root.val > maxv:
                    return (minv, root.val)
                else:
                    return (None, None)
            else:
                minvl, maxvl = helper(root.left)
                minvr, maxvr = helper(root.right)
                if minvl != None and minvr != None and maxvl < root.val and root.val < minvr:
                    return (minvl, maxvr)
                else:
                    return (None, None)

        if root == None:
            return True
        return helper(root) != (None, None)


