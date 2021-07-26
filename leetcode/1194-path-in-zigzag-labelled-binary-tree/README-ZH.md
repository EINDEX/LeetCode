# Path In Zigzag Labelled Binary Tree

## Difficulty
Medium

## Question
<p>In an infinite binary tree where every node has two children, the nodes are labelled in row order.</p>

<p>In the odd numbered rows (ie., the first, third, fifth,...), the labelling is left to right, while in the even numbered rows (second, fourth, sixth,...), the labelling is right to left.</p>

<p><img alt="" src="https://assets.leetcode.com/uploads/2019/06/24/tree.png" style="width: 300px; height: 138px;" /></p>

<p>Given the <code>label</code> of a node in this tree, return the labels in the path from the root of the tree to the&nbsp;node with that <code>label</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> label = 14
<strong>Output:</strong> [1,3,4,14]
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> label = 26
<strong>Output:</strong> [1,2,6,10,26]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= label &lt;= 10^6</code></li>
</ul>


## Solution
### golang
```golang
func pathInZigZagTree(label int) []int {

    var res []int
	for ; label > 0; {
		res = append(res, label)
		label = label >> 1
	}
	sort.Sort(sort.IntSlice(res))
	for i := len(res) - 2; i > 0; i -= 2 {
		res[i]=3*int(math.Pow(float64(2), float64(i))) - res[i] - 1
	}
    return res
}
```

## Author
EINDEX