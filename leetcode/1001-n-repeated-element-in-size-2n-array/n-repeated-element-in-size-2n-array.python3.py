class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if A[0] == A[2]:
            return A[0]
        if A[1] == A[3]:
            return A[1]
        for i in range(len(A)-1):
            if A[i] == A[i+1]:
                return A[i]
        return A[0]