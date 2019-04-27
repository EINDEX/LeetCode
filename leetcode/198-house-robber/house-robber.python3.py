class Solution:
    def rob(self, nums: List[int]) -> int:
        last = 0
        now = 0
        for i in nums:
            last, now = now, max(last + i, now)
        return now