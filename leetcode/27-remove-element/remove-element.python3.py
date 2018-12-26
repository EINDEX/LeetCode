class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        cal = 0
        for i in range(len(nums) -1, -1 , -1):
            if nums[i] == val:
                cal += 1
                for x in range(i ,len(nums) -1):
                    nums[x], nums[x+1] = nums[x+1], nums[x]
        return len(nums) - cal