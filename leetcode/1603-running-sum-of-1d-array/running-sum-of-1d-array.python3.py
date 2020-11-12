class Solution:
    x = 0
    def runningSum(self, nums: List[int]) -> List[int]:
        
        def add(n):
            self.x += n
            return self.x
        return [add(n) for n in nums]