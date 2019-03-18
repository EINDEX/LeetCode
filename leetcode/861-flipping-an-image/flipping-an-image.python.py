class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        return [[0 if i==1 else 1 for i in line[::-1]] for line in A]
        
