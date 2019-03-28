class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        rd = {}
        for a, b in zip(s, t):
            if a not in d:
                d[a] = b
            if b not in rd:
                rd[b] = a
            if d[a] != b or rd[b] != a:
                return False
            
        return True