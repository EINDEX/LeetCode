class Solution:
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int
        """
        stack = []
        for x in range(len(S)):
            if S[x] == '(':
                stack.append('(')
            else:
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(')')
                
        return len(stack)
        