from collections import deque
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        result = 0
        types = deque([-1, -1])
        b1 = 0
        b2 = 0
        i1, i2 = -1, -1
        for i in range(len(tree)):
            if tree[i] == types[0]:
                b1 += 1
                i1 = i
            elif tree[i] == types[1]:
                b2 += 1
                i2 = i
            elif types[0] == -1:
                types[0] = tree[i]
                b1 = 1
                i1 = i
            elif types[1] == -1:
                types[1] = tree[i]
                b2 = 1
                i2 = i
            else:
                result = max(result, b1 + b2)
                if tree[i-1] == types[0]:
                    b1 = i - 1 - i2
                else:
                    b1 = i - 1 - i1
                    i1 = i2
                b2 = 1
                i2 = i
                types[0] = tree[i-1]
                types[1] = tree[i]
        result = max(result, b1 + b2)
        return result
