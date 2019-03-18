class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = True
        for x in range(len(digits)-1,0-1,-1):
            # print(x)
            if flag:
                digits[x] += 1
                flag = False
            if digits[x] >= 10:
                flag = True
                digits[x] -= 10
        if flag:
            return [1] + digits
        else:
            return digits

