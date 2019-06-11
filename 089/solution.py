class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        def gen(n):
            if n == 1:
                return ["0", "1"]
            prev = gen(n-1)
            return map(lambda x: "0" + x, prev) + map(lambda x: "1" + x, reversed(prev))
        
        if n == 0:
            return [0]
        return map(lambda x: int(x, 2), gen(n))
