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
        def dfs(node, dic):
            for neighbor in node.neighbors:
                if neighbor not in dic:
                    neighborcopy = Node(neighbor.val, [])
                    dic[neighbor] = neighborcopy
                    dic[node].neighbors.append(neighborcopy)
                    dfs(neighbor, dic)
                else:
                    dic[node].neighbors.append(dic[neighbor])
                
        if not node:
            return None
        dic = {}
        nodecopy = Node(node.val, [])
        dic[node] = nodecopy
        dfs(node, dic)
        return nodecopy
