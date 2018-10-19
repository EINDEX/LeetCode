class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return A
        a, b = 0, 1
        while a < len(A) and b < len(A):
            if A[a] % 2 == 0:
                a += 2
            else:
                if A[b] % 2 == 1:
                    b += 2
                else:
                    A[a], A[b] = A[b], A[a]
        return A    
        