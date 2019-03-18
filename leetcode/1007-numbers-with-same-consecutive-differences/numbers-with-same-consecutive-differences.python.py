class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]
        if N == 0:
            return []
       
        res = []
        def inner(num, N, K):
            if N == 0:
                res.append(num)
                return
            yushu = num % 10
            if K != 0:
                if yushu - K >= 0:
                    inner(num*10+yushu-K, N-1, K)
                if yushu + K < 10:
                    inner(num*10+yushu+K, N-1, K)
            else:
                inner(num*10+yushu, N-1, K)
        for n in range(1, 10):
            inner(n, N-1, K)
        return res     
        
