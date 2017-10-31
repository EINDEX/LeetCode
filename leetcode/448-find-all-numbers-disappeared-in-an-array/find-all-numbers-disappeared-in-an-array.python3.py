class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        return list({x for x in range(1,len(nums)+1)} - set(nums)) if nums else []
