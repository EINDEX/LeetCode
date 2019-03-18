class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Python3 里 reduce 移动到 functiontools 里了
        return reduce(lambda x,n:x^n ,nums)
        

