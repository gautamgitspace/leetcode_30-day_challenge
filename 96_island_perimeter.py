ass Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows, cols, peri = len(grid), len(grid[0]), 0
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    # add 4 whenever we encounter land
                    peri += 4
                    # subtract 2 for each internal edge
                    # that contributes to the land (1)
                    if r > 0 and grid[r - 1][c] == 1:
                        peri -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        peri -= 2
        return peri
