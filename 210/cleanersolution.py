from collections import defaultdict, deque
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def dfs(i, discovered, parents, adjlist, result):
            discovered[i] = True
            parents[i] = True
            for course in adjlist[i]:
                if parents[course]:
                    return -1
                if not discovered[course]:
                    if dfs(course, discovered, parents, adjlist, result) < 0:
                        return -1
            parents[i] = False
            result.appendleft(i)
            return 0
        
        adjlist = defaultdict(list)
        for (course, pre) in prerequisites:
            adjlist[pre].append(course)
        discovered = [False for _ in range(numCourses)]
        parents = [False for _ in range(numCourses)]
        result = deque()
        for i in range(numCourses):
            if not discovered[i]:
                if dfs(i, discovered, parents, adjlist, result) < 0:
                    return []    
        if len(result) != numCourses:
            return []
        return result
