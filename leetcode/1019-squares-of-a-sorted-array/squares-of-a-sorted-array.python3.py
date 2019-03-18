#
# @lc app=leetcode.cn id=977 lang=python3
#
# [977] 不同的子序列 II
#
# https://leetcode-cn.com/problems/squares-of-a-sorted-array/description/
#
# algorithms
# Easy (74.20%)
# Total Accepted:    1.8K
# Total Submissions: 2.4K
# Testcase Example:  '[-4,-1,0,3,10]'
#
# 给定一个按非递减顺序排序的整数数组 A，返回每个数字的平方组成的新数组，要求也按非递减顺序排序。
# 
# 
# 
# 示例 1：
# 
# 输入：[-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 
# 
# 示例 2：
# 
# 输入：[-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A 已按非递减顺序排序。
# 
# 
#
class Solution:
    def sortedSquares(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        for i in range(len(A)):
            A[i] = A[i] * A[i]
        
        A.sort()
        return A

        

