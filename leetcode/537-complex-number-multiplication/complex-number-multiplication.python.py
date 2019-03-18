class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x0,x1 = self.u(a)
        y0,y1 = self.u(b)
        return "%s+%si" % (x0*y0-x1*y1,x0*y1+x1*y0)
        
    def u(self,str):
        a = ''
        b = ''
        flag = True
        for n in str[:-1]:
            if flag:
                a+=n
                if n==u'+':
                    flag = False
            else:
                b+=n
        return int(a[:-1]),int(b)
