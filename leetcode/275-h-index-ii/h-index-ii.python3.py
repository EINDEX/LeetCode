class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        for i in range(len(citations)):
            if citations[-i-1] >= i+1:
                h = i+1
            else:
                break
        return h