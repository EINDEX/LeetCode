class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        for i, x in enumerate(numbers):
            if target - x in data:
                return [data[target-x]+1, i+1]
            data[x] = i