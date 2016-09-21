class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        num_dict=collections.Counter(nums)
        return sorted(num_dict,key=num_dict.get,reverse=True)[:k]


            
        