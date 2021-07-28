class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row, column = False, False
        for i in matrix[0]:
            if i == 0:
                row = True
                break

        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                column = True
                break
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        if row:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if column:
            for i in range(len(matrix)):
                matrix[i][0] = 0