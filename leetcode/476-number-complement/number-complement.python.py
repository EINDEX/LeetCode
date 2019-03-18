class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        return num ^ (2 ** (len(bin(num)) - 2) -1)
