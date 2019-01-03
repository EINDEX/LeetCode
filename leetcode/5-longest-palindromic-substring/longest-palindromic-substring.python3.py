class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        l = len(s)
        # 单字符扩展
        for i in range(l):
            k = 0
            while i - k >= 0 and i + k < l:
                if s[i-k] == s[i+k]:
                    if 2*k+1 > len(res):
                        res = s[i-k:i+k+1]
                else:
                    break
                k += 1
                
        
        # 双字符扩展
        for i in range(l-1):
            k = 0
            while i - k >= 0 and i+1 + k < l:
                if s[i-k] == s[i+1+k]:
                    if 2*k+2 > len(res):
                        res = s[i-k:i+k+2]
                else:
                    break
                k += 1
        return res