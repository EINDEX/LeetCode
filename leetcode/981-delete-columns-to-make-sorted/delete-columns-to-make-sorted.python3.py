class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        D = set()
        for x in range(len(A[0])):
            t = A[0][x]
            for i in range(len(A)-1):
                if A[i+1][x] >= t:
                    t = A[i+1][x]
                else:
                    D.add(x)
        return len(D)
            
                