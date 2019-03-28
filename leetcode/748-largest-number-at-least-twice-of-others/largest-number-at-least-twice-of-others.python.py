class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = nums.index(max(nums))
        for i, x in enumerate(nums):
            if i != c:
                if nums[c] < x*2:
                    return -1
        return c
        