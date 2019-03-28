import copy

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        res = [0]
        h, w = len(grid), len(grid[0])
        
        t = [[0 for _ in range(w)] for _ in range(h)]
        
        start = (0, 0)
        for x in range(w):
            for y in range(h):
                if grid[y][x] == 1:
                    start = (y, x)
                elif grid[y][x] == -1:
                    t[y][x] = 1
        
        def inner(t, y, x):
            
            if x < 0 or y < 0 or x >= w or y >= h:
                return
            if t[y][x] == 1:
                return
            t =  copy.deepcopy(t)
            t[y][x] = 1
            if grid[y][x] == 2:
                if all([all(i) for i in t]):
                    res[0] += 1
                return
            inner(t, y+1, x)
            inner(t, y-1, x)
            inner(t, y, x+1)
            inner(t, y, x-1)
        
        inner(t, start[0], start[1])
        return res[0]
        