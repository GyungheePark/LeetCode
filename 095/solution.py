import copy

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def addNode(tree, cur, lastleaf):
            result = []
            if cur.right == None and cur.left == None:
                if lastleaf:
                    cur.left = TreeNode(0)
                    result.append(copy.deepcopy(tree))
                    cur.left = None
                    cur.right = TreeNode(0)
                    result.append(copy.deepcopy(tree))
                    cur.right = None
            elif cur.right == None and cur.left != None:
                result += addNode(tree, cur.left, lastleaf)
                if lastleaf:
                    cur.right = TreeNode(0)
                    result.append(copy.deepcopy(tree))
                    cur.right = None
            elif cur.right != None and cur.left == None:
                result += addNode(tree, cur.right, lastleaf)
            else:
                result += addNode(tree, cur.left, False)
                result += addNode(tree, cur.right, lastleaf)
            return result
        
        def genStructure(n):
            if n == 0:
                return []
            elif n == 1:
                return [TreeNode(0)]
            
            result = []
            for subtree in genStructure(n-1):
                result += addNode(subtree, subtree, True)
            return result
        
        def allocNums(tree, n):
            i = n
            if tree.left != None:
                i = allocNums(tree.left, n)
            tree.val = i
            i += 1
            if tree.right != None:
                i = allocNums(tree.right, i)
            return i
            
        structures = genStructure(n)
        for tree in structures:
            allocNums(tree, 1)
        return structures
