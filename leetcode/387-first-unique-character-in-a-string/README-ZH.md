# First Unique Character in a String

## Difficulty
Easy

## Question
<p>Given a string <code>s</code>, <em>find the first non-repeating character in it and return its index</em>. If it does not exist, return <code>-1</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> 0
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "loveleetcode"
<strong>Output:</strong> 2
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> s = "aabb"
<strong>Output:</strong> -1
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s</code> consists of only lowercase English letters.</li>
</ul>



## Solution
### python3
```python3
class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        bucket = {chr(k):0 for k in range(97,123)}
        for i, k in enumerate(s):
            if bucket[k] == 0:
                bucket[k] = i+1
            elif bucket[k] > 0:
                bucket[k] = -1
       
        for i, k in enumerate(s):
            if bucket[k] > 0:
                return i
        else:
            return -1

```