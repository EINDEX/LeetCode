class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        d = {}
        for i in s:
            d.setdefault(i, 0)
            d[i] += 1
        
        for i in t:
            if i not in d:
                return False
            else:
                if d[i] <= 0:
                    return False
                d[i] -= 1
        return True

