class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        p = {2,3,5,7,11,13,17,19}
        for x in range(L, R+1):
            if bin(x).count('1') in p:
                res += 1
        return res