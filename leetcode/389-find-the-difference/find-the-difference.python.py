class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        letters={}
        for l in t:
            if l not in letters:
                letters[l] = 1
            else:
                letters[l] += 1
        for b in s:
            letters[b] -= 1
        for k,v in letters.items():
            if v != 0:
                return k
        return

