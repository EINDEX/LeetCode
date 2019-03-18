class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 因为 数组中的数字都是正整数
        # 使用类似于基数排序的方式，通过修改源数据的正负号来进行 Flag 的标识，如果源数据对应的坑已小于零，就说明数据已存在。
        res = []
        for x in nums:
            if nums[abs(x)-1] < 0:
                res.append(abs(x))
            else:
                nums[abs(x)-1] *= -1
        return res

