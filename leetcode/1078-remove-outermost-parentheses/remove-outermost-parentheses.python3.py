class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        res = []
        stack = []
        last = 0
        for x in range(len(S)):
            t = S[x]
            if t == '(':
                stack.append(')')
            elif t == ')':
                stack.pop()
            
            if not stack:
                res.append(S[last:x+1])
                last = x + 1
        return ''.join(x[1:-1] for x in res)