# Valid Palindrome

## Difficulty
Easy

## Question
<p>Given a string <code>s</code>, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;A man, a plan, a canal: Panama&quot;
<strong>Output:</strong> true
<strong>Explanation:</strong> &quot;amanaplanacanalpanama&quot; is a palindrome.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> s = &quot;race a car&quot;
<strong>Output:</strong> false
<strong>Explanation:</strong> &quot;raceacar&quot; is not a palindrome.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= s.length &lt;= 2 * 10<sup>5</sup></code></li>
	<li><code>s</code> consists only of printable ASCII characters.</li>
</ul>



## Solution
### python3
```python3
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        a = 0
        b = len(s) - 1
        def isV(v):
            if 97 <= ord(v) <= 122:
                return True
            if 65 <= ord(v) <= 90:
                return True
            if 48 <= ord(v) <= 57:
                return True
        while a < b:
            if not isV(s[a]):
                a += 1
                continue
            if not isV(s[b]):
                b -= 1
                continue
            if s[a].lower() == s[b].lower():
                a += 1
                b -= 1
            else:
                return False
        return True
```