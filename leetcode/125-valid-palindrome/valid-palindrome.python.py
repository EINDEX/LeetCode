class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        b = len(s) - 1
        def isV(v):
            if 97 <= ord(v) <= 122:
                return True
            if 65 <= ord(v) <= 90:
                return True
            if 48 <= ord(v) <= 57:
                return True
        while a < b:
            if not isV(s[a]):
                a += 1
                continue
            if not isV(s[b]):
                b -= 1
                continue
            if s[a].lower() == s[b].lower():
                a += 1
                b -= 1
            else:
                return False
        return True
