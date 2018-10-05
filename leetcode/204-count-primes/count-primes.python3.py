class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0
        res = [True]*n
        res[0], res[1] = False, False
        
        for i in range(2, n):
            if i * i >= n:
                break
                
            if not res[i]:
                continue
            
            for j in range(i*i, n, i):
                res[j] = False
        
        return sum(res)
                        
        