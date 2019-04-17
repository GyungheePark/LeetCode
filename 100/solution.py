# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None:
            if q == None:
                return True
            else:
                return False
        if q == None:
            return False
        if p.val == q.val:
            if p.left != None:
                if q.left != None:
                    if not self.isSameTree(p.left, q.left):
                        return False
                else:
                    return False
            else:
                if q.left != None:
                    return False
            if p.right != None:
                if q.right != None:
                    if not self.isSameTree(p.right, q.right):
                        return False
                else:
                    return False
            else:
                if q.right != None:
                    return False
            return True
        return False
                    
