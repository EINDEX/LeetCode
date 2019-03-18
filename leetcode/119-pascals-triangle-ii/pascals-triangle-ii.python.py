class Solution:
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]
        res = [0 for x in range(rowIndex+1)]
        res[0],res[1] = 1, 1
        for x in range(1, rowIndex):
            for k in range(x,0-1,-1):
                res[k+1] = res[k] + res[k+1]
            res[x+1] = 1
        return res
            
            
        
