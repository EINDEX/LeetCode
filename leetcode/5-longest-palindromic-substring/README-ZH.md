# Longest Palindromic Substring

## Difficulty
Medium

## Question
<p>Given a string <code>s</code>, return&nbsp;<em>the longest palindromic substring</em> in <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;babad&quot;
<strong>Output:</strong> &quot;bab&quot;
<strong>Note:</strong> &quot;aba&quot; is also a valid answer.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;cbbd&quot;
<strong>Output:</strong> &quot;bb&quot;
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;a&quot;
<strong>Output:</strong> &quot;a&quot;
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;ac&quot;
<strong>Output:</strong> &quot;a&quot;
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 1000</code></li>
	<li><code>s</code> consist of only digits and English letters (lower-case and/or upper-case),</li>
</ul>



## Solution
### python3
```python3
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = len(s)
        if l < 2 or s == s[::-1]:
            return s
        
        start = 0
        max_len = 0
        # 单字符扩展
        for i in range(l):
            k = 0
            while i - k >= 0 and i + k < l:
                if s[i-k] == s[i+k]:
                    if 2*k+1 > max_len:
                        start = i-k
                        max_len = 2*k+1
                else:
                    break
                k += 1
            k = 0
            while i - k >= 0 and i+1 + k < l:
                if s[i-k] == s[i+1+k]:
                    if 2*k+2 > max_len:
                        start = i-k
                        max_len = 2*k+2
                else:
                    break
                k += 1
                
        return s[start:start+max_len]
```