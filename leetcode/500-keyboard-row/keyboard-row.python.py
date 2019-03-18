class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        a, b, c = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        f = lambda x,y : set(x.lower()).issubset(y)
        return  [w for w in words if f(w,a) or f(w,b) or f(w,c)]
        
