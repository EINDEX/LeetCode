class Solution:
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ls = 0
        rs = sum(nums[1:])

        for i, x in enumerate(nums):
            if ls == rs:
                return i
            ls += x
            if i < len(nums) - 1:
                rs -= nums[i+1]
        return -1


