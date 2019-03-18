class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        start = False
        is_low_of_zero = False
        res = ""
        for x in str:
            if start == False:
                if x == ' ':
                    continue
                elif x == '+':
                    is_low_of_zero = False
                elif x == '-':
                    is_low_of_zero = True
                elif x.isdigit():
                    res += x
                else:
                    return 0
                start = True
            else:
                if x.isdigit():
                    res += x
                else:
                    break
        if not res:
            return 0
        
        res = int(res)    
        if res > 2147483647:
            res = 2147483647
            if is_low_of_zero:
                res = 2147483648
        
        return -res if is_low_of_zero else res
        

