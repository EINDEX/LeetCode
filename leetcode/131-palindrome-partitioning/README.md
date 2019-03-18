# Palindrome Partitioning

## Difficulty
Medium

## Question
<p>Given a string <code>s</code>, partition <code>s</code> such that every substring of the partition is a <strong>palindrome</strong>. Return all possible palindrome partitioning of <code>s</code>.</p>

<p>A <strong>palindrome</strong> string is a string that reads the same backward as forward.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "aab"
<strong>Output:</strong> [["a","a","b"],["aa","b"]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "a"
<strong>Output:</strong> [["a"]]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 16</code></li>
	<li><code>s</code> contains only lowercase English letters.</li>
</ul>



## Solution
### python
```python
class Solution:
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        def inner(l, s): 
            if s and len(s) > 1:
                for x in range(1, len(s)+1):
                    if s[:x] == s[:x][::-1]:
                        c = l[:]
                        c.append(s[:x])
                        inner(c, s[x:])
            else:
                c = l[:]
                if s:   
                    c.append(s)
                if all([x==x[::-1] for x in c]):
                    res.append(c)             
        inner([], s)
        return res
        

```