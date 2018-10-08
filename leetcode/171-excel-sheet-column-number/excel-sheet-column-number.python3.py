class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        return sum([(ord(x)-(ord('A')-1))*(26**(len(s)-i-1))  for i, x in enumerate(list(s))])
        