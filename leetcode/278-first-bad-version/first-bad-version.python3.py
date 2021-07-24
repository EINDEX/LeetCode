# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, h = 1, n
        i = l + h // 2
        f = False
        while l < h:
            if not isBadVersion(i):
                l = i + 1
                f = True   
            elif isBadVersion(i):
                h = i - 1
                f = False
            i = l + (h-l)//2
        return i + int(not isBadVersion(i))