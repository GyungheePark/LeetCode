class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            sa, ea = A[i]
            sb, eb = B[j]
            if ea < sb:
                i += 1
            elif eb < sa:
                j += 1
            elif sa <= sb <= ea:
                if eb <= ea:
                    result.append([sb, eb])
                    j += 1
                else:
                    result.append([sb, ea])
                    i += 1
            elif sb <= sa <= eb:
                if ea <= eb:
                    result.append([sa, ea])
                    i += 1
                else:
                    result.append([sa, eb])
                    j += 1
        return result
