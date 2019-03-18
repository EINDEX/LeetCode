class Solution:
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        def inner(nums, k, n):
            if k == 0 and n == 0:
                res.append(nums)
            if len(nums) and n < nums[-1]:
                return
            if k == 0:
                return
            if not nums:
                m = 1
            else:
                m = nums[-1] + 1
            M = n // k+1
            if M > 10:
                M = 10
            for x in range(m, M):
                inner(nums+[x], k-1, n-x)
            
        inner([], k, n)
        return res
            
        
