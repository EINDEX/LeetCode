class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        t = [ n for num in nums for n in num] 
        if r*c != len(t): return nums
        return [[t.pop(0) for _ in range(c)] for __ in range(r)]

        
        
        
        

