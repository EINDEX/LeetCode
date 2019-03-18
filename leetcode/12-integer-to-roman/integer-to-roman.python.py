class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        res += (num // 1000)*'M'
        num %= 1000
        res += (num // 900) * 'CM'
        num %= 900
        res += (num // 500) * 'D'
        num %= 500
        res += (num // 400) * 'CD'
        num %= 400
        res += (num // 100) * 'C'
        num %= 100
        res += (num // 90) * 'XC'
        num %= 90
        res += (num // 50) * 'L'
        num %= 50
        res += (num // 40) * 'XL'
        num %= 40
        res += (num // 10) * 'X'
        num %= 10
        res += (num // 9) * 'IX'
        num %= 9
        res += (num // 5) * 'V'
        num %= 5
        res += (num // 4) * 'IV'
        num %= 4
        res += (num // 1) * 'I'
        return res
