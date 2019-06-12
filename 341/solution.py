# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        def flatten(nestedInteger):
            if nestedInteger.isInteger():
                return [nestedInteger.getInteger()]
            result = []
            for n in nestedInteger.getList():
                result += flatten(n)
            return result
        self.list = []
        for n in nestedList:
            self.list += flatten(n)
        self.index = 0
        self.size = len(self.list)
        
    def next(self):
        """
        :rtype: int
        """
        self.index += 1
        return self.list[self.index - 1]

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.index < self.size
    
# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
