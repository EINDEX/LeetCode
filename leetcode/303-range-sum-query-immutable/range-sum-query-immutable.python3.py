class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.results = []
        if not nums:
            return
        self.results.append(nums[0])
        for x in range(1, len(nums)):
            self.results.append(self.results[x-1]+nums[x])
            

    def sumRange(self, i: int, j: int) -> int:
        if i <= 0:
            m = 0
        else:
            m = self.results[i-1]
        
        return self.results[j] - m


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)