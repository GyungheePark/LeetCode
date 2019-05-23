# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def aux(root, p, q):
            pflag, qflag = False, False
            if root.val == p.val:
                pflag = True
            elif root.val == q.val:
                qflag = True
            
            lpflag, lqflag, lnode = False, False, None
            if root.left:
                lpflag, lqflag, lnode = aux(root.left, p, q)
            if lpflag and lqflag:
                return lpflag, lqflag, lnode
            pflag |= lpflag
            qflag |= lqflag
            if pflag and qflag:
                return pflag, qflag, root
            rpflag, rqflag, rnode = False, False, None
            if root.right:
                rpflag, rqflag, rnode = aux(root.right, p, q)
            if rpflag and rqflag:
                return rpflag, rqflag, rnode
            pflag |= rpflag
            qflag |= rqflag
            if pflag and qflag:
                return pflag, qflag, root
            else:
                return pflag, qflag, None
        
        _, _, node = aux(root, p, q)
        return node
