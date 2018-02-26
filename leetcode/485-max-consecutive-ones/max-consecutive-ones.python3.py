class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_value = 0
        count = 0
        flag = True
        for x in nums:
            if x == 0:
                flag = False
            else:
                if not flag:
                    count = 0
                count += 1
                flag = True
                if count > max_value:
                    max_value = count
        return max_value
