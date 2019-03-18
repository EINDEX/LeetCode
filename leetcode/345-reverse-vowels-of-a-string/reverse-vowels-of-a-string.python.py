class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = set('aeiouAEIOU')
        s = list(s)
        a, b = 0, len(s) - 1
        while a < b:
            if s[a] not in yuan:
                a += 1
                continue
            if s[b] not in yuan:
                b -= 1
                continue
            s[a], s[b] = s[b],  s[a]
            a += 1
            b -= 1
        return ''.join(s)
        
        
