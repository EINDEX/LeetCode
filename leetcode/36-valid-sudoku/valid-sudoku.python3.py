class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for i in range(9)]
        cols = [set() for i in range(9)]
        boxs = [set() for i in range(9)]
        
        for x in range(9):
            for y in range(9):
                t = board[x][y]
                if t == '.':
                    continue
     
                if t not in rows[x]:
                    rows[x].add(t)
                else:
                    return False
                
                if t not in cols[y]:
                    cols[y].add(t)
                else:
                    return False
                
                bid = x//3 + (y//3)*3
                if t not in boxs[bid]:
                    boxs[bid].add(t)
                else:
                    return False
        return True
                    