# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        # bfs solution
        queue = deque(nestedList)
        depth = 1
        total = 0
        while queue:
            for _ in range(len(queue)):
                ni = queue.popleft()
                if ni.isInteger():
                    total += ni.getInteger() * depth
                else:
                    for elem in ni.getList():
                        queue.append(elem)
            depth += 1
        return total

        # dfs solution
        def rec(depth, nl):
            if nl.isInteger():
                return depth * nl.getInteger()
            res = 0
            for elem in nl.getList():
                res += rec(depth + 1, elem)
            return res

        total = 0
        for nested_integer in nestedList:
            total += rec(1, nested_integer)
        return total