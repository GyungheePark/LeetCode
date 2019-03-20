class Solution(object):
    table = {0:[], 1:["()"]}
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n in self.table.keys():
            return self.table[n]

        result = set()
        for p in self.generateParenthesis(n-1):
            result.add("(" + p + ")")

        i = 1
        while i <=  n/2:
            for p1 in self.generateParenthesis(i):
                for p2 in self.generateParenthesis(n-i):
                    result.add(p1+p2)
                    result.add(p2+p1)
            i += 1

        self.table[n] = list(result)
        return self.table[n]
