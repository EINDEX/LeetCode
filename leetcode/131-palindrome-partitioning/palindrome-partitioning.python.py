class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def inner(l, s): 
            if s and len(s) > 1:
                for x in range(1, len(s)+1):
                    if s[:x] == s[:x][::-1]:
                        c = l[:]
                        c.append(s[:x])
                        inner(c, s[x:])
            else:
                c = l[:]
                if s:   
                    c.append(s)
                if all([x==x[::-1] for x in c]):
                    res.append(c)             
        inner([], s)
        return res
        
