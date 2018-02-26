class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i,x in enumerate(nums):
            if target - x in nums:
                i2 = nums.index(target - x)
                if  i2 != i:
                    return [i,i2]
        
