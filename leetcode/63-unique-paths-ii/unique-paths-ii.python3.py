class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        w = len(obstacleGrid[0])
        h = len(obstacleGrid)
        
        for x in range(w):
            for y in range(h):
                if x == 0 and y == 0:
                    if obstacleGrid[y][x] != 1:
                        obstacleGrid[y][x] = -1
                    else:
                        obstacleGrid[y][x] = 0
                    continue
                if obstacleGrid[y][x] == 1:
                    obstacleGrid[y][x] = 0
                    continue
                a = obstacleGrid[y-1][x] if y > 0 else 0
                b = obstacleGrid[y][x-1] if x > 0 else 0
                obstacleGrid[y][x] = a + b
        return -obstacleGrid[-1][-1]