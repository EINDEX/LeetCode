# Reverse String

## Difficulty
Easy

## Question
<p>Write a function that reverses a string. The input string is given as an array of characters <code>s</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> s = ["h","e","l","l","o"]
<strong>Output:</strong> ["o","l","l","e","h"]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> s = ["H","a","n","n","a","h"]
<strong>Output:</strong> ["h","a","n","n","a","H"]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 10<sup>5</sup></code></li>
	<li><code>s[i]</code> is a <a href="https://en.wikipedia.org/wiki/ASCII#Printable_characters" target="_blank">printable ascii character</a>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Do not allocate extra space for another array. You must do this by modifying the input array <a href="https://en.wikipedia.org/wiki/In-place_algorithm" target="_blank">in-place</a> with <code>O(1)</code> extra memory.</p>



## Solution
### java
```java
public class Solution {
    public String reverseString(String s) {
        StringBuilder sb=new StringBuilder(s);
        sb.reverse();
        return sb.toString();
    }
}
```
### python3
```python3
class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        return s[::-1]
        

```