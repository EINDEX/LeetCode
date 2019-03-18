class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        s = str(bin(n))[2:]
        for x in range(len(s)-1):
            if s[x] == s[x+1]:
                return False
        return True
