class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows = [[True for _ in range(9)] for _ in range(9)]
        cols = [[True for _ in range(9)] for _ in range(9)]
        boxs = [[True for _ in range(9)] for _ in range(9)]
        
        for x in range(9):
            for y in range(9):
                t = board[x][y]
                if t == '.':
                    continue
                t = int(t) - 1
                rows[x][t] = False
                cols[y][t] = False
                bid = x//3 + (y//3)*3
                boxs[bid][t] = False
                
        self.dfs(board, rows, cols, boxs)
        
    def dfs(self, board, rows, cols, boxs, x=0, y=0):
        while board[x][y] != '.':
            x += 1
            if x > 8:
                x = 0
                y += 1
            if y > 8:
                return True
        
        for k in range(9):
            bid = x//3 + (y//3)*3
            if rows[x][k] and cols[y][k] and boxs[bid][k]:
                board[x][y] = str(k+1)
                rows[x][k] = False
                cols[y][k] = False
                boxs[bid][k] = False
                if self.dfs(board, rows, cols, boxs, x, y):
                    return True
                else:
                    board[x][y] = '.'
                    rows[x][k] = True
                    cols[y][k] = True
                    boxs[bid][k] = True
                    
        return False