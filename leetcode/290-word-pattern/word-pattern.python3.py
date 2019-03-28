class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(words) != len(pattern):
            return False
        
        d = {}
        rd = {}
        
        for a, b in zip(pattern, words):
            if a not in d:
                d[a] = b
            if b not in rd:
                rd[b] = a
            if d[a] != b or rd[b] != a:
                return False
            
        return True