class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        return [i[0] for i in sorted([(i, sum(x)) for i, x in enumerate(mat)], key=lambda x:x[1])[:k]]