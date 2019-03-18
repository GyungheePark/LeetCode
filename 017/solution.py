class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dic = {"2": list("abc"), "3":list("def"), "4":list("ghi"), "5":list("jkl"), "6":list("mno"), "7":list("pqrs"), "8":list("tuv"), "9":list("wxyz")}
        result = []
        for s in digits:
            if result == []:
                pref = [""]
            else:
                pref = result
            result = []
            for p in pref:
                for l in dic[s]:
                    result.append(p+l)
        return result
        
