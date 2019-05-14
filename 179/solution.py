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
        
        result = "".join(sorted(list(map(str, nums)), cmp = compare, reverse = True))
        if result[0] == '0':
            return "0"
        else:
            return result
