class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int

        x >
        11110
        11010
        11000
        00000 y ^
        """
        count = 0
        y = len(grid)
        if y == 0: return 0
        x = len(grid[0])
        # visit each element in grid and if
        # its 1, mark it for 0 (destroy it)
        # and keep a count for it
        for i in range(0,y):
            for j in range(0, x):
                if grid[i][j] == '1':
                    self.dfs_mark(grid, i, j)
                    count += 1
        return count


    def dfs_mark(self, grid, i, j):
        y = len(grid)
        x = len(grid[0])
        # check for invalid elements and for sites that are NOT LAND
        if i < 0 or j < 0 or i >= y or j >= x or grid[i][j] != '1': return
        # mark it
        grid[i][j] = '0'
        # check adjacent
        self.dfs_mark(grid, i+1, j)
        self.dfs_mark(grid, i-1, j)
        self.dfs_mark(grid, i, j+1)
        self.dfs_mark(grid, i, j-1)
