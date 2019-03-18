from functools import reduce
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = lambda z: reduce(lambda x,y :x*y, range(1, z+1)) if z > 0 else 1
        return int(a(m+n-2)/(a(m-1)*a(n-1)))
        
        
