# Numbers With Same Consecutive Differences

## Difficulty
Medium

## Question
<p>Return all <strong>non-negative</strong> integers of length <code>n</code> such that the absolute difference between every two consecutive digits is <code>k</code>.</p>

<p>Note that <strong>every</strong> number in the answer <strong>must not</strong> have leading zeros. For example, <code>01</code> has one leading zero and is invalid.</p>

<p>You may return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> n = 3, k = 7
<strong>Output:</strong> [181,292,707,818,929]
<strong>Explanation:</strong> Note that 070 is not a valid number, because it has leading zeroes.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> n = 2, k = 1
<strong>Output:</strong> [10,12,21,23,32,34,43,45,54,56,65,67,76,78,87,89,98]
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> n = 2, k = 0
<strong>Output:</strong> [11,22,33,44,55,66,77,88,99]
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> n = 2, k = 2
<strong>Output:</strong> [13,20,24,31,35,42,46,53,57,64,68,75,79,86,97]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= n &lt;= 9</code></li>
	<li><code>0 &lt;= k &lt;= 9</code></li>
</ul>



## Solution
### python
```python
class Solution:
    def numsSameConsecDiff(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: List[int]
        """
        if N == 1:
            return [0,1,2,3,4,5,6,7,8,9]
        if N == 0:
            return []
       
        res = []
        def inner(num, N, K):
            if N == 0:
                res.append(num)
                return
            yushu = num % 10
            if K != 0:
                if yushu - K >= 0:
                    inner(num*10+yushu-K, N-1, K)
                if yushu + K < 10:
                    inner(num*10+yushu+K, N-1, K)
            else:
                inner(num*10+yushu, N-1, K)
        for n in range(1, 10):
            inner(n, N-1, K)
        return res     
        

```