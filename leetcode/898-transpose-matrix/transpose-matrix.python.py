class Solution:
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[A[x][y] for x in range(len(A))] for y in range(len(A[0]))]
        
        
