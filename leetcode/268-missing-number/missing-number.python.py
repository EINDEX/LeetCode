class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        b = 0
        for x in range(l+1):
            b ^= x
        for x in nums:
            b  ^= x
        return b
