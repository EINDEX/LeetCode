class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        num_set=set()
        for n in nums:
            if n not in num_set:
                num_set.add(n)
            else:
                num_set.remove(n)
        return list(num_set)
