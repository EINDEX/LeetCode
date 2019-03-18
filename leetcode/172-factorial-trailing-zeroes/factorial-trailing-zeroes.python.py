class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 1
        res = 0
        while True:
            k = n // (5 ** count)
            if k == 0:
                break
            res += k
            count += 1
        return res


