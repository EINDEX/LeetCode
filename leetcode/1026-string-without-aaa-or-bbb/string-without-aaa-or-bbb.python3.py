#
# @lc app=leetcode.cn id=984 lang=python3
#
# [984] 移除最多的同行或同列石头
#
# https://leetcode-cn.com/problems/string-without-aaa-or-bbb/description/
#
# algorithms
# Easy (25.39%)
# Total Accepted:    540
# Total Submissions: 2.1K
# Testcase Example:  '1\n2'
#
# 给定两个整数 A 和 B，返回任意字符串 S，要求满足：
# 
# 
# S 的长度为 A + B，且正好包含 A 个 'a' 字母与 B 个 'b' 字母；
# 子串 'aaa' 没有出现在 S 中；
# 子串 'bbb' 没有出现在 S 中。
# 
# 
# 
# 
# 示例 1：
# 
# 输入：A = 1, B = 2
# 输出："abb"
# 解释："abb", "bab" 和 "bba" 都是正确答案。
# 
# 
# 示例 2：
# 
# 输入：A = 4, B = 1
# 输出："aabaa"
# 
# 
# 
# 提示：
# 
# 
# 0 <= A <= 100
# 0 <= B <= 100
# 对于给定的 A 和 B，保证存在满足要求的 S。
# 
# 
#
class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        res = ''
        if A > B:
            flag = False
        else:
            flag = True
        while A or B:
            if A == 0:
                res += B * 'b'
                B = 0
            elif B == 0:
                res += A * 'a'
                A = 0 
            elif A > 2*B:
                res += 'aa'
                A -= 2
                res += 'b'
                B -= 1
            elif 2 * A < B:
                res += 'bb'
                B -= 2
                res += 'a'
                A -= 1
            else:
                if not flag:
                    res += 'ab'
                else:
                    res += 'ba'
                A -= 1
                B -= 1
        return res
        

