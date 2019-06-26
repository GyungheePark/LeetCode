class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        for i in range(1, n + 1):
            v = ""
            if i % 3 == 0:
                v += "Fizz"
            if i % 5 == 0:
                v += "Buzz"
            if not v:
                v += str(i)
            result.append(v)
        return result
