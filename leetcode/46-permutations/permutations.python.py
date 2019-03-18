class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # 每次从已有数字中选取一个数字然后进入下一次迭代
        res = []
        def inner(num, nums):
            for n in nums:
                inner(num+[n], [i for i in nums if i !=n])
            if not nums:
                res.append(num)
        
        inner([], nums)
        return res
