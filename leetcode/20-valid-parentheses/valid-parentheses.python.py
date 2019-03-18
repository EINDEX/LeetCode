class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        t = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        stack = []
        flag = True
        for x in range(len(s)):
            if s[x] in t:
                if stack:
                    if stack[-1] == t[s[x]]:
                        stack.pop(-1)
                    else:
                        return False
                else:
                    return False
            else:
                stack.append(s[x])
        if stack:
            return False
        return True
