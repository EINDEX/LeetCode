class Solution:
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        da = {}
        for a in A.split():
            da.setdefault(a,0)
            da[a] += 1
        
        for b in B.split():
            da.setdefault(b, 0)
            da[b] += 1
        return [x for x,v in da.items() if v == 1]
            
