# Reverse Vowels of a String

## Difficulty
Easy

## Question
<p>Given a string <code>s</code>, reverse only all the vowels in the string and return it.</p>

<p>The vowels are <code>&#39;a&#39;</code>, <code>&#39;e&#39;</code>, <code>&#39;i&#39;</code>, <code>&#39;o&#39;</code>, and <code>&#39;u&#39;</code>, and they can appear in both cases.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = "hello"
<strong>Output:</strong> "holle"
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = "leetcode"
<strong>Output:</strong> "leotcede"
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 3 * 10<sup>5</sup></code></li>
	<li><code>s</code> consist of <strong>printable ASCII</strong> characters.</li>
</ul>



## Solution
### python3
```python3
class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        yuan = ('a', 'e', 'i', 'o', 'u', 'A','E','I','O', 'U')
        r = []
        for x in range(len(s)):
            if s[x] in yuan:
                r.append(s[x])
        k = 1
        s = list(s)
        for x in range(len(s)):
            if s[x] in yuan:
                s[x] = r[-k]
                k += 1
        return ''.join(s)
        
        
```