# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        L=1
        R=n
        res=0
        while L<=R:
            mid= R-((R-L)>>1)
            res=guess(mid)
            if res == 0:
                return mid
            elif res == 1:
                L=mid+1
            else:
                R=mid-1
        return L

