from functools import reduce
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == 1 or n == 1:
            return 1
        a = lambda z: reduce(lambda x,y :x*y, range(1, z+1)) if z > 0 else 1
        return int(a(m+n-2)/(a(m-1)*a(n-1)))
        
        