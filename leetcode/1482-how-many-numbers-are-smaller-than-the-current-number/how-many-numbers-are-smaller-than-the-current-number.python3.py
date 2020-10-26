class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [sum([1 for i in nums if i < n]) for n in nums]