class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        row = len(grid[0])
        cos = len(grid)
        s = 0
        for r in range(row):
            for c in range(cos):
                if grid[c][r]:
                    count = 0
                    if r > 0:
                        if grid[c][r-1]:
                            count += 1
                    if r < row - 1:
                        if grid[c][r+1]:
                            count += 1
                    if c > 0:
                        if grid[c-1][r]:
                            count += 1
                    if c < cos - 1:
                        if grid[c+1][r]:
                            count += 1
                    s += 4 - count
        return s
        

