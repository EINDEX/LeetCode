# Sort Array By Parity II

## Difficulty
Easy

## Question
<p>Given an array of integers <code>nums</code>, half of the integers in <code>nums</code> are <strong>odd</strong>, and the other half are <strong>even</strong>.</p>

<p>Sort the array so that whenever <code>nums[i]</code> is odd, <code>i</code> is <strong>odd</strong>, and whenever <code>nums[i]</code> is even, <code>i</code> is <strong>even</strong>.</p>

<p>Return <em>any answer array that satisfies this condition</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> nums = [4,2,5,7]
<strong>Output:</strong> [4,5,2,7]
<strong>Explanation:</strong> [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> nums = [2,3]
<strong>Output:</strong> [2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>nums.length</code> is even.</li>
	<li>Half of the integers in <code>nums</code> are even.</li>
	<li><code>0 &lt;= nums[i] &lt;= 1000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow Up:</strong> Could you solve it in-place?</p>



## Solution
### python3
```python3
class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        if not A:
            return A
        a, b = 0, 1
        while a < len(A) and b < len(A):
            if A[a] % 2 == 0:
                a += 2
            else:
                if A[b] % 2 == 1:
                    b += 2
                else:
                    A[a], A[b] = A[b], A[a]
        return A    
        
```