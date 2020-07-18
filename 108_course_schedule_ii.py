class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        same logic as course schedule 1.

        not visited = 0, being visited = -1, visited done = 1
        do dfs and keep capturing i in res when visited done
        and return res
        """
        graph = [[] for _ in xrange(numCourses)]
        visited = [0 for _ in xrange(numCourses)]
        res = []

        # generate graph
        for x, y in prerequisites:
            graph[x].append(y)

        for i in range(numCourses):
            if not self.dfs(graph, visited, i, res):
                return []
        return res

    def dfs(self, graph, visited, i, res):
        if visited[i] == -1:
            return False
        if visited[i] == 1:
            return True
        # being visited
        visited[i] = -1
        for j in graph[i]:
            if not self.dfs(graph, visited, j, res):
                return False
        visited[i] = 1
        res.append(i)
        return True
