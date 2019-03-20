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
        prev = self.generateParenthesis(n-1)
        for p in prev:
            result.add("(" + p + ")")
        
        i = 1
        while i <=  n/2:
            prev1 = self.generateParenthesis(i)
            prev2 = self.generateParenthesis(n-i)
            for p1 in prev1:
                for p2 in prev2:
                    result.add(p1+p2)
                    result.add(p2+p1)
            i += 1
            
        self.table[n] = list(result)
        return list(result)
