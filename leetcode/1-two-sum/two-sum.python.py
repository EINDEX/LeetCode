class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        for i, x in enumerate(nums):
            if target - x in data:
                return [data[target-x], i]
            data[x] = i
