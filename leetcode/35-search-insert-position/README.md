# Search Insert Position

## Difficulty
Easy

## Question
<p>Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.</p>

<p>You must&nbsp;write an algorithm with&nbsp;<code>O(log n)</code> runtime complexity.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5,6], target = 5
<strong>Output:</strong> 2
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5,6], target = 2
<strong>Output:</strong> 1
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5,6], target = 7
<strong>Output:</strong> 4
</pre><p><strong>Example 4:</strong></p>
<pre><strong>Input:</strong> nums = [1,3,5,6], target = 0
<strong>Output:</strong> 0
</pre><p><strong>Example 5:</strong></p>
<pre><strong>Input:</strong> nums = [1], target = 0
<strong>Output:</strong> 0
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>4</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
	<li><code>nums</code> contains <strong>distinct</strong> values sorted in <strong>ascending</strong> order.</li>
	<li><code>-10<sup>4</sup> &lt;= target &lt;= 10<sup>4</sup></code></li>
</ul>



## Solution
### python3
```python3
#
# @lc app=leetcode.cn id=35 lang=python3
#
# [35] 搜索插入位置
#
# https://leetcode-cn.com/problems/search-insert-position/description/
#
# algorithms
# Easy (42.19%)
# Total Accepted:    26.7K
# Total Submissions: 63.3K
# Testcase Example:  '[1,3,5,6]\n5'
#
# 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
# 
# 你可以假设数组中无重复元素。
# 
# 示例 1:
# 
# 输入: [1,3,5,6], 5
# 输出: 2
# 
# 
# 示例 2:
# 
# 输入: [1,3,5,6], 2
# 输出: 1
# 
# 
# 示例 3:
# 
# 输入: [1,3,5,6], 7
# 输出: 4
# 
# 
# 示例 4:
# 
# 输入: [1,3,5,6], 0
# 输出: 0
# 
# 
#
class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target < nums[0]:
            return 0
        elif target > nums[-1]:
            return len(nums)
        l = 0
        h = len(nums)
        # if h == 0 and nums[0] == target:
            # return 0
        while l < h:
            m = (l + h) // 2 
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                h = m - 1
        if target >  nums[l]:
            return l + 1
        return l
        
        


```