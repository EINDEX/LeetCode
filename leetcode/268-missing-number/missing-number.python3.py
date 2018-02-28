class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = ((len(nums) + 0) * (len(nums)+1)//2)
        return s - sum(nums)
