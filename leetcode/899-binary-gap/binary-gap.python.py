class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        res = 0
        flag = False
        last_1 = 0
        for i, x in enumerate(str(bin(N))):
            if x == '1':
                if flag:
                    if i - last_1 > res:
                        res = i - last_1
                last_1 = i
                flag = True
                
        return res
