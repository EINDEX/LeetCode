class Solution:
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def inner(nums, min_value, k):
            if k == 0:
                res.append(nums)
                return
            if min_value > n:
                return
            for x in range(min_value, n+1):
                inner(nums+[x], x+1,  k-1)
        
        inner([], 1, k)
        return res
        