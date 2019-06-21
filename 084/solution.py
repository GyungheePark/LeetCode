class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        result = 0
        stack = []
        for curx, curh in enumerate(heights):
            if not stack:
                stack.append((curx, curh))
            else:
                x, h = stack[-1]
                newcurx = curx
                while h > curh:
                    stack.pop()
                    result = max(result, (curx - x) * h)
                    newcurx = x
                    if stack:
                        x, h = stack[-1]
                    else:
                        break
                stack.append((newcurx, curh))
        while stack:
            x, h = stack.pop()
            result = max(result, (len(heights) - x) * h)
        return result
