"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        def connectHelper(root, leftinright):
            if leftinright == None:
                root.next = None
                lefts = [root]
                if root.right and root.left:
                    (right, rlefts) = connectHelper(root.right, None)
                    (left, llefts) = connectHelper(root.left, rlefts)
                    left.next = right
                    lefts += llefts
                return (root, lefts)
            else:
                root.next = leftinright[0]
                lefts = [root]
                if root.right and root.left:
                    (right, rlefts) = connectHelper(root.right, leftinright[1:])
                    (left, llefts) = connectHelper(root.left, rlefts)
                    left.next = right
                    lefts += llefts
                return (root, lefts)
        
        if not root:
            return root
        return connectHelper(root, None)[0]
