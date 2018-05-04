class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if not nums1 or not nums2:
            return []
        
        data = {}
        for x in nums1:
            data.setdefault(x,0)
            data[x] += 1
        
        res = []
        for x in nums2:
            if x in data and data[x]>0:
                data[x]-=1
                res.append(x)
                
        return res