# Sum of Even Numbers After Queries

## Difficulty
Easy

## Question
<p>We have an array <code>nums</code> of integers, and an array <code>queries</code>&nbsp;of queries.</p>

<p>For the <code>i</code>-th&nbsp;query <code>val =&nbsp;queries[i][0], index&nbsp;= queries[i][1]</code>, we add <font face="monospace">val</font>&nbsp;to <code>nums[index]</code>.&nbsp; Then, the answer to the <code>i</code>-th query is the sum of the even values of <code>A</code>.</p>

<p><em>(Here, the given <code>index = queries[i][1]</code> is a 0-based index, and each query permanently modifies the array <code>nums</code>.)</em></p>

<p>Return the answer to all queries.&nbsp; Your <code>answer</code> array should have&nbsp;<code>answer[i]</code>&nbsp;as&nbsp;the answer to the <code>i</code>-th query.</p>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input: </strong>nums = <span id="example-input-1-1">[1,2,3,4]</span>, queries = <span id="example-input-1-2">[[1,0],[-3,1],[-4,0],[2,3]]</span>
<strong>Output: </strong><span id="example-output-1">[8,6,2,4]</span>
<strong>Explanation: </strong>
At the beginning, the array is [1,2,3,4].
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
</pre>

<p>&nbsp;</p>

<p><strong>Note:</strong></p>

<ol>
	<li><code>1 &lt;= nums.length &lt;= 10000</code></li>
	<li><code>-10000 &lt;= nums[i] &lt;= 10000</code></li>
	<li><code>1 &lt;= queries.length &lt;= 10000</code></li>
	<li><code>-10000 &lt;= queries[i][0] &lt;= 10000</code></li>
	<li><code>0 &lt;= queries[i][1] &lt; nums.length</code></li>
</ol>



## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=985 lang=python3
#
# [985] 令牌放置
#
# https://leetcode-cn.com/problems/sum-of-even-numbers-after-queries/description/
#
# algorithms
# Easy (68.70%)
# Total Accepted:    405
# Total Submissions: 590
# Testcase Example:  '[1,2,3,4]\n[[1,0],[-3,1],[-4,0],[2,3]]'
#
# 给出一个整数数组 A 和一个查询数组 queries。
# 
# 对于第 i 次查询，有 val = queries[i][0], index = queries[i][1]，我们会把 val 加到 A[index]
# 上。然后，第 i 次查询的答案是 A 中偶数值的和。
# 
# （此处给定的 index = queries[i][1] 是从 0 开始的索引，每次查询都会永久修改数组 A。）
# 
# 返回所有查询的答案。你的答案应当以数组 answer 给出，answer[i] 为第 i 次查询的答案。
# 
# 
# 
# 示例：
# 
# 输入：A = [1,2,3,4], queries = [[1,0],[-3,1],[-4,0],[2,3]]
# 输出：[8,6,2,4]
# 解释：
# 开始时，数组为 [1,2,3,4]。
# 将 1 加到 A[0] 上之后，数组为 [2,2,3,4]，偶数值之和为 2 + 2 + 4 = 8。
# 将 -3 加到 A[1] 上之后，数组为 [2,-1,3,4]，偶数值之和为 2 + 4 = 6。
# 将 -4 加到 A[0] 上之后，数组为 [-2,-1,3,4]，偶数值之和为 -2 + 4 = 2。
# 将 2 加到 A[3] 上之后，数组为 [-2,-1,3,6]，偶数值之和为 -2 + 6 = 4。
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# 1 <= queries.length <= 10000
# -10000 <= queries[i][0] <= 10000
# 0 <= queries[i][1] < A.length
# 
# 
#
class Solution:
    def sumEvenAfterQueries(self, A: 'List[int]', queries: 'List[List[int]]') -> 'List[int]':
        res = []
        s = sum([x for x in A if x % 2 == 0])
        for i in queries:
            if A[i[1]] % 2 == 0:
                if i[0] % 2 == 0:
                    s += i[0]
                else:
                    s -= A[i[1]]
            else:
                if i[0] % 2:
                    s += A[i[1]] + i[0]
                
            A[i[1]] += i[0]
            res.append(s)

        return res      


```