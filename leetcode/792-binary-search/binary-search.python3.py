class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, h = 0, len(nums) - 1
        i = l + h // 2
        while l <= h:
            if nums[i] <  target:
                l = i + 1
            elif nums[i] >  target:
                h = i - 1
            else:
                return i
            i = l+(h-l)//2
        return -1