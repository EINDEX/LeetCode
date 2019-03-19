class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix) == 1:
            return
        l = len(matrix)
        m = matrix
        for x in range(l):
            for y in range(x,l):
                if x != y:
                    m[x][y], m[y][x] = m[y][x], m[x][y]
        for x in range(l):
            m[x] = m[x][::-1]