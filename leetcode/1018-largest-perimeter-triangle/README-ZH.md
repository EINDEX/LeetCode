# Largest Perimeter Triangle

## Difficulty
Easy

## Question
<p>Given an integer array <code>nums</code>, return <em>the largest perimeter of a triangle with a non-zero area, formed from three of these lengths</em>. If it is impossible to form any triangle of a non-zero area, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [2,1,2]
<strong>Output:</strong> 5
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,1]
<strong>Output:</strong> 0
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [3,2,3,4]
<strong>Output:</strong> 10
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> nums = [3,6,2,3]
<strong>Output:</strong> 8
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>3 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>1 &lt;= nums[i] &lt;= 10<sup>6</sup></code></li>
</ul>



## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=976 lang=python3
#
# [976] 最小面积矩形
#
# https://leetcode-cn.com/problems/largest-perimeter-triangle/description/
#
# algorithms
# Easy (57.06%)
# Total Accepted:    1.5K
# Total Submissions: 2.6K
# Testcase Example:  '[2,1,2]'
#
# 给定由一些正数（代表长度）组成的数组 A，返回由其中三个长度组成的、面积不为零的三角形的最大周长。
# 
# 如果不能形成任何面积不为零的三角形，返回 0。
# 
# 
# 
# 
# 
# 
# 示例 1：
# 
# 输入：[2,1,2]
# 输出：5
# 
# 
# 示例 2：
# 
# 输入：[1,2,1]
# 输出：0
# 
# 
# 示例 3：
# 
# 输入：[3,2,3,4]
# 输出：10
# 
# 
# 示例 4：
# 
# 输入：[3,6,2,3]
# 输出：8
# 
# 
# 
# 
# 提示：
# 
# 
# 3 <= A.length <= 10000
# 1 <= A[i] <= 10^6
# 
# 
#
class Solution:
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort(reverse=True)
        for i in range(len(A) - 3 + 1):
            if A[i] < A[i+1] + A[i+2]:
                return A[i] + A[i+1] + A[i+2]
        else:
            return 0        
        

```