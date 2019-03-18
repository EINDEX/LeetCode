#
# @lc app=leetcode.cn id=949 lang=python3
#
# [949] 猫和老鼠
#
# https://leetcode-cn.com/problems/largest-time-for-given-digits/description/
#
# algorithms
# Easy (27.98%)
# Total Accepted:    780
# Total Submissions: 2.8K
# Testcase Example:  '[1,2,3,4]'
#
# 给定一个由 4 位数字组成的数组，返回可以设置的符合 24 小时制的最大时间。
# 
# 最小的 24 小时制时间是 00:00，而最大的是 23:59。从 00:00 （午夜）开始算起，过得越久，时间越大。
# 
# 以长度为 5 的字符串返回答案。如果不能确定有效时间，则返回空字符串。
# 
# 
# 
# 示例 1：
# 
# 输入：[1,2,3,4]
# 输出："23:41"
# 
# 
# 示例 2：
# 
# 输入：[5,5,5,5]
# 输出：""
# 
# 
# 
# 
# 提示：
# 
# 
# A.length == 4
# 0 <= A[i] <= 9
# 
# 
#
class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        A.sort()
        for x in range(23, -1, -1):
            x = str(x)
            if len(x) == 1:
                x = '0' + x
            print(x)
            if int(x[0]) != int(x[1]):
                if int(x[0]) not in A or int(x[1]) not in A:
                    continue
            else:
                if A.count(int(x[0])) < 2:
                    continue
            for y in range(59, -1, -1):
                y = str(y)
                if len(y) == 1:
                    y = '0' + y
                r = [int(c) for c in x + y]
                r.sort()
                if all([r[x] == A[x] for x in range(4)]):
                    return x + ':' + y 
        return ''

