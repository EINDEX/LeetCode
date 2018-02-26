class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        res = []
        for x in range(1, numRows+1):
            if x == 1:
                res.append([1])
            else:
                line = []
                for i in range(x):
                    if i == 0:
                        line.append(1)
                    elif i == x - 1:
                        line.append(1)
                    else:
                        line.append(res[-1][i-1]+res[-1][i])
                res.append(line)
        return res
    
