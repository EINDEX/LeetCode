# Integer to Roman

## Difficulty
Medium

## Question
<p>Roman numerals are represented by seven different symbols:&nbsp;<code>I</code>, <code>V</code>, <code>X</code>, <code>L</code>, <code>C</code>, <code>D</code> and <code>M</code>.</p>

<pre>
<strong>Symbol</strong>       <strong>Value</strong>
I             1
V             5
X             10
L             50
C             100
D             500
M             1000</pre>

<p>For example,&nbsp;<code>2</code> is written as <code>II</code>&nbsp;in Roman numeral, just two one&#39;s added together. <code>12</code> is written as&nbsp;<code>XII</code>, which is simply <code>X + II</code>. The number <code>27</code> is written as <code>XXVII</code>, which is <code>XX + V + II</code>.</p>

<p>Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not <code>IIII</code>. Instead, the number four is written as <code>IV</code>. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as <code>IX</code>. There are six instances where subtraction is used:</p>

<ul>
	<li><code>I</code> can be placed before <code>V</code> (5) and <code>X</code> (10) to make 4 and 9.&nbsp;</li>
	<li><code>X</code> can be placed before <code>L</code> (50) and <code>C</code> (100) to make 40 and 90.&nbsp;</li>
	<li><code>C</code> can be placed before <code>D</code> (500) and <code>M</code> (1000) to make 400 and 900.</li>
</ul>

<p>Given an integer, convert it to a roman numeral.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> num = 3
<strong>Output:</strong> &quot;III&quot;
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> num = 4
<strong>Output:</strong> &quot;IV&quot;
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> num = 9
<strong>Output:</strong> &quot;IX&quot;
</pre>

<p><strong>Example 4:</strong></p>

<pre>
<strong>Input:</strong> num = 58
<strong>Output:</strong> &quot;LVIII&quot;
<strong>Explanation:</strong> L = 50, V = 5, III = 3.
</pre>

<p><strong>Example 5:</strong></p>

<pre>
<strong>Input:</strong> num = 1994
<strong>Output:</strong> &quot;MCMXCIV&quot;
<strong>Explanation:</strong> M = 1000, CM = 900, XC = 90 and IV = 4.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= num &lt;= 3999</code></li>
</ul>



## Solution
### python
```python
class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        res += (num // 1000)*'M'
        num %= 1000
        res += (num // 900) * 'CM'
        num %= 900
        res += (num // 500) * 'D'
        num %= 500
        res += (num // 400) * 'CD'
        num %= 400
        res += (num // 100) * 'C'
        num %= 100
        res += (num // 90) * 'XC'
        num %= 90
        res += (num // 50) * 'L'
        num %= 50
        res += (num // 40) * 'XL'
        num %= 40
        res += (num // 10) * 'X'
        num %= 10
        res += (num // 9) * 'IX'
        num %= 9
        res += (num // 5) * 'V'
        num %= 5
        res += (num // 4) * 'IV'
        num %= 4
        res += (num // 1) * 'I'
        return res

```