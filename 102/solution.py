from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        if root == None:
            return []
        result = []
        q = deque()
        q.append((root, 0))
        while q:
            node, i = q.popleft()
            if len(result) <= i:
                result.append([node.val])
            else:
                result[i].append(node.val)    
            if node.left:
                q.append((node.left, i+1))
            if node.right:
                q.append((node.right, i+1))
        return result


