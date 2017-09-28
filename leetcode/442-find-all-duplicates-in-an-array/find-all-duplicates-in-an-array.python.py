class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 因为 数组中的数字都是正整数
        # 让我们可以使用类似于基数排序的方式，将元数据散列到新的空间上，如果重复出现的值，就添加到结果中 。
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res