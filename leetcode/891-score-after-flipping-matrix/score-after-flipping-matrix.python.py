class Solution:
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # 按行翻转保证第一列的值都为正
        # 第二列往后和小于 1/2 行数是翻转列
        if not A:
            return 0
        
        # 翻转行
        for x in range(len(A)):
            if A[x][0] == 0:  
                for y in range(len(A[x])):
                    if A[x][y] == 0:
                        A[x][y] = 1
                    else:
                        A[x][y] = 0
        s = 0
        # 算和
        for y in range(len(A[0])):
            line_s = sum([A[x][y] for x in range(len(A))])
            s += max(len(A) - line_s, line_s) * (2**(len(A[0])-y-1))
        return s
            
