# Verifying an Alien Dictionary

## Difficulty
Easy

## Question
<p>In an alien language, surprisingly they also use english lowercase letters, but possibly&nbsp;in a different <code>order</code>. The&nbsp;<code>order</code> of the alphabet&nbsp;is some permutation&nbsp;of lowercase letters.</p>

<p>Given a sequence of <code>words</code>&nbsp;written in the alien language,&nbsp;and the <code>order</code> of the alphabet,&nbsp;return <code>true</code> if and only if the given <code>words</code>&nbsp;are sorted lexicographicaly in this alien language.</p>
<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;hello&quot;,&quot;leetcode&quot;], order = &quot;hlabcdefgijkmnopqrstuvwxyz&quot;
<strong>Output:</strong> true
<strong>Explanation: </strong>As &#39;h&#39; comes before &#39;l&#39; in this language, then the sequence is sorted.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;word&quot;,&quot;world&quot;,&quot;row&quot;], order = &quot;worldabcefghijkmnpqstuvxyz&quot;
<strong>Output:</strong> false
<strong>Explanation: </strong>As &#39;d&#39; comes after &#39;l&#39; in this language, then words[0] &gt; words[1], hence the sequence is unsorted.
</pre>

<p><strong>Example 3:</strong></p>

<pre>
<strong>Input:</strong> words = [&quot;apple&quot;,&quot;app&quot;], order = &quot;abcdefghijklmnopqrstuvwxyz&quot;
<strong>Output:</strong> false
<strong>Explanation: </strong>The first three characters &quot;app&quot; match, and the second string is shorter (in size.) According to lexicographical rules &quot;apple&quot; &gt; &quot;app&quot;, because &#39;l&#39; &gt; &#39;&empty;&#39;, where &#39;&empty;&#39; is defined as the blank character which is less than any other character (<a href="https://en.wikipedia.org/wiki/Lexicographical_order" target="_blank">More info</a>).
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= words.length &lt;= 100</code></li>
	<li><code>1 &lt;= words[i].length &lt;= 20</code></li>
	<li><code>order.length == 26</code></li>
	<li>All characters in <code>words[i]</code> and <code>order</code> are English lowercase letters.</li>
</ul>



## Solution
### python3
```python3
class Solution:
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        table = {}
        ourtable = "abcdefghijklmnopqrstuvwxyz"
        for i, x in enumerate(order):
            table[x] = ourtable[i]
        def toOurWord(word):
            word = list(word)
            for i in range(len(word)):
                word[i] = table[word[i]]
            return ''.join(word)
        temp = toOurWord(words[0])
        for i in range(len(words)-1):
            c = toOurWord(words[i+1])
            if c < temp:
                return False
            temp = c
        return True
```