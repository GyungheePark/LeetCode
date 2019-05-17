class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        def dfs(adjList, pre, checked, visited, stack):
            if pre in checked:
                return True
            visited.add(pre)
            checked.add(pre)
            if pre not in adjList:
                return True
            stack[pre] = True
            for course in adjList[pre]:
                if course not in visited:
                    if not dfs(adjList, course, checked, visited, stack):
                        return False
                elif stack[course]:
                    return False
            stack[pre] = False
            return True
        
        adjList = {}
        for pre, course in prerequisites:
            if pre in adjList:
                adjList[pre].append(course)
            else:
                adjList[pre] = [course]
        
        checked = set()
        stack = [False for _ in range(numCourses)]
        for pre in adjList:
            if pre not in checked:
                visited = set()
                if not dfs(adjList, pre, checked, visited, stack):
                    return False
        return True
