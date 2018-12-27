class Solution:
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        deck.sort(reverse=True)
        
        res = []
        for x in deck:
            if res:
                res = res[-1:] + res[0:-1]
            res = [x] + res
        return res
        