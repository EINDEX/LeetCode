class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            x = -x
            res = -int(str(x)[::-1])
        else:
            res = int(str(x)[::-1])
        if res < - 2**31:
            return 0
        elif res > 2**31 -1:
            return 0
        else:
            return res
        

