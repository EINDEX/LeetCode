class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for n in xrange(1, len(s)+1):
            for x in xrange(len(s)-n+1):
                if s[x:x+n] == s[x:x+n][::-1]:
                    count += 1
        return count
        