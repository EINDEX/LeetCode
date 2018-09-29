class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        res = []
        for word in words:
            status = True
            data = {}
            for i in range(len(word)):
                if pattern[i] not in data:
                    data[pattern[i]] = word[i]
                else:
                    if data[pattern[i]] != word[i]:
                        status = False
                        break
            if len(set(data.keys())) != len(set(data.values())):
                status = False
                
            if status:
                res.append(word)
        return res
        