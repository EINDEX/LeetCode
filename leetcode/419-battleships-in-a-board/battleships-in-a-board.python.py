class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        for x,y in [ (x,y) for x in range(len(board)) for y in range(len(board[0]))][::-1]:
            if board[x][y] == 'X':
                if ((y > 0 and board[x][y-1] != 'X') or y == 0) and ((x > 0 and board[x-1][y] != 'X') or x == 0 ):
                    count += 1
        return count                
        
            
        
