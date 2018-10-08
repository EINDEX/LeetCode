class Solution:
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        res = 0
        h, w = len(grid), len(grid[0])
        def area(x, y):
            if x< 0 or x >= w or y <0 or y>=h:
                return 0
            if grid[y][x]:
                grid[y][x] = 0
                return area(x+1, y) + area(x-1,y) + area(x, y+1) + area(x, y-1) + 1
            return 0
        
        for x in range(w):
            for y in range(h):
                if grid[y][x]:
                    res = max(area(x, y), res)
        return res
                