# 连续子数组的最大和  LCOF

## Difficulty
Easy

## Question
English description is not available for the problem. Please switch to Chinese.


## Solution
### python3
```python3
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        for x in range(1, len(nums)):
            if nums[x-1] > 0:
                nums[x] += nums[x-1]
        return max(nums)
        

```