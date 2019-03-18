class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        t = nums[-k:]
        

        for x in range(len(nums) - 1, k-1, -1):
            nums[x] = nums[x-k]
        
        for x in range(len(t)):
            nums[x] = t[x]
       