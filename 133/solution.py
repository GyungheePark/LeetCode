from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None
        dic = {}
        nodecopy = Node(node.val, [])
        dic[node] = nodecopy
        q = deque()
        q.append(node)
        while q:
            node = q.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborcopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborcopy
                    q.append(neighbor)
                    dic[node].neighbors.append(neighborcopy)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodecopy
