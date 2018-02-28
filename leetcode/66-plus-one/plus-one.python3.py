class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = False
        digits[-1] += 1
        for i in range(len(digits)-1, 0-1, -1):
            if flag:
                digits[i] += 1
                flag = False
            if digits[i] >= 10:
                digits[i] -= 10
                flag = True
        else:
            if flag:
                digits = [1] + digits
        return digits
                
