from collections import deque
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
        
        q = deque()
        q.append((root, 0))
        lastnode = []
        if not root:
            return root
        while q:
            node, i = q.popleft()
            node.next = None
            if i >= len(lastnode):
                lastnode.append(node)
            else:
                lastnode[i].next = node
                lastnode[i] = node
            if node.left and node.right:
                q.append((node.left, i+1))
                q.append((node.right, i+1))
        return root
