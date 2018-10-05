class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        bottom = [0 for _ in range(len(grid[0]))]
        right = [max(x) for x in grid]
        for line in grid:
            for i,x in enumerate(line):
                if bottom[i] < x:
                    bottom[i] = x
        s = 0
        for x in range(len(grid)):
            for y in range(len(grid[0])):
                s += min(bottom[x], right[y]) - grid[x][y]
        return s
                
            
            
        