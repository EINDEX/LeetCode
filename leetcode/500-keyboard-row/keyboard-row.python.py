class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r = []
        row = ["qwertyuiop","asdfghjkl","zxcvbnm"]
        for word in words:
            for i in range(3):
                flag = True
                for a in word.lower():
                    if a not in row[i]:
                        flag = False
                if flag:
                    r.append(word)
        return r
                        
                
            