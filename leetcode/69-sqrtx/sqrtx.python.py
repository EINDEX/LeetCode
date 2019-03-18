class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        l = 0
        h = x // 2 + 1
        mid = 0

        while(l <= h):
            mid = (l+h) // 2
            if mid ** 2 > x:
                h = mid - 1
            elif mid ** 2 < x:
                l = mid + 1
            else:
                return mid
        return (l+h) // 2



