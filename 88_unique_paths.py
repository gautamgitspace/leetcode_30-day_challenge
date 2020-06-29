class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 0 or n<= 0:
            return 0
        if m == 1 or n == 1:
            return 1

        # build matrix, cols first then rows
        matrix = [[1 for j in range(n)]for i in range(m)]

        for i in range (1, m):
            for j in range(1, n):
                matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1]
        return matrix[-1][-1]
        
