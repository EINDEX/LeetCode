# Largest Time for Given Digits

## Difficulty
Medium

## Question
<p>Given an array&nbsp;<code>arr</code> of 4 digits, find the latest 24-hour time that can be made using each digit <strong>exactly once</strong>.</p>

<p>24-hour times are formatted as <code>&quot;HH:MM&quot;</code>, where <code>HH</code>&nbsp;is between&nbsp;<code>00</code>&nbsp;and&nbsp;<code>23</code>, and&nbsp;<code>MM</code>&nbsp;is between&nbsp;<code>00</code>&nbsp;and&nbsp;<code>59</code>. The earliest 24-hour time is <code>00:00</code>, and the latest is <code>23:59</code>.</p>

<p>Return <em>the latest 24-hour time&nbsp;in&nbsp;<code>&quot;HH:MM&quot;</code> format</em>.&nbsp; If no valid time can be made, return an empty string.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> arr = [1,2,3,4]
<strong>Output:</strong> &quot;23:41&quot;
<strong>Explanation:</strong>&nbsp;The valid 24-hour times are &quot;12:34&quot;, &quot;12:43&quot;, &quot;13:24&quot;, &quot;13:42&quot;, &quot;14:23&quot;, &quot;14:32&quot;, &quot;21:34&quot;, &quot;21:43&quot;, &quot;23:14&quot;, and &quot;23:41&quot;. Of these times, &quot;23:41&quot; is the latest.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> arr = [5,5,5,5]
<strong>Output:</strong> &quot;&quot;
<strong>Explanation:</strong>&nbsp;There are no valid 24-hour times as &quot;55:55&quot; is not valid.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> arr = [0,0,0,0]
<strong>Output:</strong> &quot;00:00&quot;
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> arr = [0,0,1,0]
<strong>Output:</strong> &quot;10:00&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>arr.length == 4</code></li>
	<li><code>0 &lt;= arr[i] &lt;= 9</code></li>
</ul>



## Solution
### python3
```python3
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

```