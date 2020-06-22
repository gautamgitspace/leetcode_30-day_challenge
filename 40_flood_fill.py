class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        row, col = len(image), len(image[0])
        color = image[sr][sc]

        def dfs(i, j):
            # boundary sanity check
            if i < 0 or i >= row or j < 0 or j >= col:
                return
            # if pixel already newColor or pixel not same as color
            if image[i][j] == newColor or image[i][j] != color:
                return
            # begin at sr, sc
            image[i][j] = newColor
            # f'in spread it
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        dfs(sr, sc)
        return image
