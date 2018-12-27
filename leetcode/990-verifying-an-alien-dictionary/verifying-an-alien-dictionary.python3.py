class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        table = {}
        ourtable = "abcdefghijklmnopqrstuvwxyz"
        for i, x in enumerate(order):
            table[x] = ourtable[i]
        def toOurWord(word):
            word = list(word)
            for i in range(len(word)):
                word[i] = table[word[i]]
            return ''.join(word)
        temp = toOurWord(words[0])
        for i in range(len(words)-1):
            c = toOurWord(words[i+1])
            if c < temp:
                return False
            temp = c
        return True