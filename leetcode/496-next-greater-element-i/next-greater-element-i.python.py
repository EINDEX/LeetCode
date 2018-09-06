class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        def b():
            x = nums.index(n)
            for c in range(x,len(nums)-1):
                a = nums[c+1]
                if a > n:
                    return a
            else:
                return -1
        for n in findNums:
            ans.append(b())
            
        return ans
