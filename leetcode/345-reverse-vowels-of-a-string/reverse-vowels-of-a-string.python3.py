class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = ('a', 'e', 'i', 'o', 'u', 'A','E','I','O', 'U')
        r = []
        for x in range(len(s)):
            if s[x] in yuan:
                r.append(s[x])
        k = 1
        s = list(s)
        for x in range(len(s)):
            if s[x] in yuan:
                s[x] = r[-k]
                k += 1
        return ''.join(s)
        
        