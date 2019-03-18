class Solution:
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        l = len(nums)
        res = 0
        tmp = nums[0] - 1
        count = 0
        for x in range(l):
            if nums[x] > tmp:
                count += 1
                if count > res:
                    res = count
            else:
                count = 1
            tmp = nums[x]
        return res
            


