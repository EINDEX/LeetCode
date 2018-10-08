class Solution:
    def smallestRangeI(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        M = 0
        m = 9999999999999999999
        for x in A:
            if x > M:
                M = x
            if x < m:
                m = x
        if M - K < m + K:
            return 0
        else:
            return M-m-2*K
        