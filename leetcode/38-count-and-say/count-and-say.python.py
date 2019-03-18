class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        x = '1'
        def inner(x,n):
            if n == 0:
                return '1'
            c = x[0]
            table = []
            tv = 0
            for t in x:
                if t == c:  
                    tv += 1
                elif tv != 0:
                    table.append((tv,c))
                    tv = 1
                    c = t
            if tv:
                table.append((tv, c))
            res = "".join([str(x)+y for x,y in table])
            if n == 1:
                return res
            return inner(res, n-1)
        if n == 0:
            return ''
        else:
            return inner(x, n-1)
        
