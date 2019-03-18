class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if not nums:
            return []
        zi = len(nums)
        flag = False
        for i in range(len(nums)):
            if nums[i] == 0 and not flag:
                zi = i
                flag = True
            elif zi < len(nums):
                nums[i], nums[zi] = nums[zi], nums[i]
                while zi<len(nums) and  nums[zi]:
                    zi += 1
