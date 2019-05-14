import itertools
import functools
class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        def compare(x, y):
            if x == y:
                return 0
            if x+y > y+x:
                return 1
            else:
                return -1
        
        result = "".join(sorted(list(map(str, nums)), key = functools.cmp_to_key(compare), reverse=True))
        result = list(itertools.dropwhile(lambda x: x == '0', result[:-1])) + [result[-1]]
        return ''.join(result)
