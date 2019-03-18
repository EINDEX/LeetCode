class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        #v2
        return bin(x^y).count('1')
    
        #v1
        a = bin(x)[2:]
        b = bin(y)[2:]
        if len(a) < len(b):
            a='0'*(len(b)-len(a))+a
        else:
            b='0'*(len(a)-len(b))+b
        return sum([a!=b for a,b in zip(a,b)])
        

