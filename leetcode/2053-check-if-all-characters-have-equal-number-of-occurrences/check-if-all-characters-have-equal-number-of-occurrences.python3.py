class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        d = {}
        for a in list(s):
            d.setdefault(a, 0)
            d[a] += 1
        return len(set(d.values())) == 1