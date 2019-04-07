import re

t = re.compile('[A-Z][a-z]{0,}')

class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        res = []
        p =[re.compile('[a-z]{0,}'.join(list(x))+'[a-z]{0,}') for x in t.findall(pattern)]
        print(p)
            
        def check(q):
            qs = t.findall(q)
            if len(qs) != len(p):
                return False
            for a, b in zip(p, qs):
                if not a.fullmatch(b):
                    return False
            return True
        
        for q in queries:
            res.append(check(q))
        return res
            