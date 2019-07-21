import re

class Solution:
    def maskPII(self, S: str) -> str:
        if '@' in S:
            s = S.lower()
            a, b = s.split('@')
            return a[0] + '*****' + a[-1] + '@' + b
        
        numbers = []
        for x in range(len(S)):
            if S[x].isdigit():
                numbers.append(S[x])
        if len(numbers) == 10:
            return '***-***-' + ''.join(numbers[-4:])
        elif len(numbers) > 10:
            return f'+{(len(numbers)-10)*"*"}-***-***-' + ''.join(numbers[-4:])
            