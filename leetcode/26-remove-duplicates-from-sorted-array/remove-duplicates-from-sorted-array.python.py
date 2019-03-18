class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        x = nums[0]
        for n in nums[1:]:
            if n == x:
                nums.remove(n)
            else:
                x = n
        return len(nums)

