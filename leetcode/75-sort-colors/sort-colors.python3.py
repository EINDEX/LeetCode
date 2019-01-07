class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r = 0
        w = 0
        b = 0
        for x in nums:
            if x == 0:
                r += 1
            elif x == 1:
                w += 1
            elif x == 2:
                b += 1
        for x in range(len(nums)):
            if x < r:
                nums[x] = 0
            elif x < w+r:
                nums[x] = 1
            elif x < w+r+b:
                nums[x] = 2