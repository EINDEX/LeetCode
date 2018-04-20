class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        majority = nums[0]
        count = 1
        for x in nums[1:]:
            if x == majority:
                count += 1
            else:
                count -= 1
                if count < 0:
                    majority = x
                    count = 0
        return majority
