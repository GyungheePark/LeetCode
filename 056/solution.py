# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals = sorted(intervals, key = lambda i: i.start)
        result = []
        if len(intervals) <= 1:
            return intervals
        i, j = 0, 1
        while j < len(intervals):
            while j < len(intervals) and intervals[j].start <= intervals[i].end:
                if intervals[j].end >= intervals[i].end:
                    intervals[i].end = intervals[j].end
                j += 1
            result.append(intervals[i])
            i = j
            j += 1
        if i < len(intervals):
            result.append(intervals[i])
        return result
