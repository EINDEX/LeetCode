# Powerful Integers

## Difficulty
Medium

## Question
<p>Given three integers <code>x</code>, <code>y</code>, and <code>bound</code>, return <em>a list of all the <strong>powerful integers</strong> that have a value less than or equal to</em> <code>bound</code>.</p>

<p>An integer is <strong>powerful</strong> if it can be represented as <code>x<sup>i</sup> + y<sup>j</sup></code> for some integers <code>i &gt;= 0</code> and <code>j &gt;= 0</code>.</p>

<p>You may return the answer in <strong>any order</strong>. In your answer, each value should occur <strong>at most once</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> x = 2, y = 3, bound = 10
<strong>Output:</strong> [2,3,4,5,7,9,10]
<strong>Explanation:</strong>
2 = 2<sup>0</sup> + 3<sup>0</sup>
3 = 2<sup>1</sup> + 3<sup>0</sup>
4 = 2<sup>0</sup> + 3<sup>1</sup>
5 = 2<sup>1</sup> + 3<sup>1</sup>
7 = 2<sup>2</sup> + 3<sup>1</sup>
9 = 2<sup>3</sup> + 3<sup>0</sup>
10 = 2<sup>0</sup> + 3<sup>2</sup>
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> x = 3, y = 5, bound = 15
<strong>Output:</strong> [2,4,6,8,10,14]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= x, y &lt;= 100</code></li>
	<li><code>0 &lt;= bound &lt;= 10<sup>6</sup></code></li>
</ul>



## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=970 lang=python3
#
# [970] Powerful Integers
#
# https://leetcode-cn.com/problems/powerful-integers/description/
#
# algorithms
# Easy (38.29%)
# Total Accepted:    918
# Total Submissions: 2.4K
# Testcase Example:  '2\n3\n10'
#
# 给定两个非负整数 x 和 y，如果某一整数等于 x^i + y^j，其中整数 i >= 0 且 j >= 0，那么我们认为该整数是一个强整数。
# 
# 返回值小于或等于 bound 的所有强整数组成的列表。
# 
# 你可以按任何顺序返回答案。在你的回答中，每个值最多出现一次。
# 
# 
# 
# 示例 1：
# 
# 输入：x = 2, y = 3, bound = 10
# 输出：[2,3,4,5,7,9,10]
# 解释： 
# 2 = 2^0 + 3^0
# 3 = 2^1 + 3^0
# 4 = 2^0 + 3^1
# 5 = 2^1 + 3^1
# 7 = 2^2 + 3^1
# 9 = 2^3 + 3^0
# 10 = 2^0 + 3^2
# 
# 
# 示例 2：
# 
# 输入：x = 3, y = 5, bound = 15
# 输出：[2,4,6,8,10,14]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= x <= 100
# 1 <= y <= 100
# 0 <= bound <= 10^6
# 
# 
#
import math

class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        if bound == 0:
            return []
        res = set()
        
        for i in range(int(math.log(bound, x)+1) if x != 1 else 1):
            for j in range(int(math.log(bound, y)+1) if y != 1 else 1):
                r = x**i + y ** j
                if r > bound:
                    break
                res.add(r) 
        return list(res)

```