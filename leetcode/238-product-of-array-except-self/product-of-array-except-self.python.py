class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = 1
        zeros = 0
        index = None
        for i,n in enumerate(nums):
            if n == 0:
                zeros +=1
                index = i
            else:
                res *= n
        if zeros >=2:
            return [0]*len(nums)
        elif zeros == 1:
            l = [0]*len(nums)
            l[index] = res
            return l
        return [res/s for s in nums]
