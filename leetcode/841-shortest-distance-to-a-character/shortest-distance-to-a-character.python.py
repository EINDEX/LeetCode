class Solution:
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        res = [10000 for _ in range(len(S))]
        has_C = False
        last_C = 0
        for x in range(len(S)):
            if S[x] == C:
                has_C = True
                last_C = x
            if has_C:
                res[x] = x - last_C
        has_C = False
        last_C = 0
        for x in range(len(S)-1,0-1,-1):
            if S[x] == C:
                has_C = True
                last_C = x
            if has_C and last_C - x < res[x]:
                res[x] = last_C - x
        
        return res
