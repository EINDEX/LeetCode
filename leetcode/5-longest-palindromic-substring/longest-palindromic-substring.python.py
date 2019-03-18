class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2 or s == s[::-1]:
            return s
        
        start = 0
        max_len = 0
        # 单字符扩展
        for i in range(l):
            k = max_len // 2
            while i - k >= 0 and i + k < l and s[i-k:i+k+1] == s[i-k:i+k+1][::-1]:
                start = i-k
                max_len = 2*k+1
                k += 1
            k = max_len // 2
            while i - k >= 0 and i + 1 + k < l and s[i-k:i+k+2] == s[i-k:i+k+2][::-1]:
                start = i-k
                max_len = 2*k+2
                k += 1   
        return s[start:start+max_len]
