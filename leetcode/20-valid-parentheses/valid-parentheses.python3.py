class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for x in s:
            if x == ']':
                if not stack:
                    return False
                if stack[-1] == '[':
                        stack.pop(-1)
                else:
                        return False
            elif x == '}':
                    if not stack:
                        return False
                    if stack[-1] == '{':
                        stack.pop(-1)
                    else:
                        return False
            elif x == ')':
                    if not stack:
                        return False
                    if stack[-1] == '(':
                        stack.pop(-1)
                    else:
                        return False
            
            else:
                stack.append(x)
        if stack:
            return False
        return True
        