from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        def dfs(i, time, stack, discovered, finish, adjlist):
            time += 1
            discovered[i] = True
            for course in adjlist[i]:
                if course in stack:
                    return -1
                if not discovered[course]:
                    stack.append(course)
                    time = dfs(course, time, stack, discovered, finish, adjlist)
                    if time < 0:
                        return -1
            time += 1
            finish[i] = (i, time)
            stack.pop()
            return time
        
        nonroots = set()
        adjlist = defaultdict(list)
        for (course, pre) in prerequisites:
            adjlist[pre].append(course)
            nonroots.add(course)
        roots = set(range(numCourses)) - nonroots
        discovered = [False for _ in range(numCourses)]
        finish = [(i, 0) for i in range(numCourses)]
        stack = []
        time = 0
        for root in roots:
            if not discovered[root]:
                stack.append(root)
                time = dfs(root, time, stack, discovered, finish, adjlist)
                if time < 0:
                    return []
        if discovered != [True for _ in range(numCourses)]:
            return []
        finish.sort(key=lambda x:x[1], reverse = True)
        return [x[0] for x in finish]
