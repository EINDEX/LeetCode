class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        def inner(nums,low_value, candidates, target):
            if target == 0:
                res.append(nums)
            elif target < low_value:
                return
            for x in candidates:
                if x >= low_value:
                    inner(nums+[x],x, candidates, target-x)
        inner([],0, candidates, target)
        return res
        
