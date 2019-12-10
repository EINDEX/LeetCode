# Lexicographical Numbers

## Difficulty
Medium

## Question
<p>Given an integer <code>n</code>, return all the numbers in the range <code>[1, n]</code> sorted in lexicographical order.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and uses <code>O(1)</code> extra space.&nbsp;</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> n = 13
<strong>Output:</strong> [1,10,11,12,13,2,3,4,5,6,7,8,9]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> [1,2]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 5 * 10<sup>4</sup></code></li>
</ul>



## Solution
### golang
```golang
func Dfs(res *[]int, i, max int) {
	if i > max {
		return
	}
	*res = append(*res, i)
	for j := 0; j < 10; j++ {
		Dfs(res, i*10+j, max)
	}
}

func lexicalOrder(n int) []int {
    res := make([]int, 0)
	for i := 1; i <= n && i < 10; i++ {
		Dfs(&res, i, n)
	}
    return res
}
```