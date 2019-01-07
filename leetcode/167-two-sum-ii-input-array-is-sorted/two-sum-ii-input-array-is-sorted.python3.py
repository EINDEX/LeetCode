class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        for i, x in enumerate(numbers):
            if x in data:
                return [data[x]+1, i+1]
            data[target-x] = i