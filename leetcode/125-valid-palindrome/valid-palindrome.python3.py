class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = [x for x in s.lower() if x in "1234567890asdfghjklqwertyuiopzxcvbnm"]
        return s[::-1] == s
        
