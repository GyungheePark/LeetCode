class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]
        result = []
        start = None
        end = None
        inserted = False
        for interval in intervals:
            if start == None:
                if newInterval[0] <= interval[1]:
                    if newInterval[1] >= interval[0]:
                        start = min(newInterval[0], interval[0])
                        end = max(newInterval[1], interval[1])
                    else:
                        start, end = newInterval
                        result.append([start, end])
                        result.append(interval)
                        inserted = True
                else:
                    result.append(interval)
            else:
                if interval[0] <= newInterval[1]:
                    if interval[1] > end:
                        end = interval[1]
                else:
                    if not inserted:
                        result.append([start,end])
                        inserted = True
                    result.append(interval)
        if not inserted:
            if start == None:
                result.append(newInterval)
            else:
                result.append([start, end])
        return result
