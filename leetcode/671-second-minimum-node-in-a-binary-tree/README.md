# Second Minimum Node In a Binary Tree

## Difficulty
Easy

## Question
<p>Given a non-empty special binary tree consisting of nodes with the non-negative value, where each node in this tree has exactly <code>two</code> or <code>zero</code> sub-node. If the node has two sub-nodes, then this node&#39;s value is the smaller value among its two sub-nodes. More formally, the property&nbsp;<code>root.val = min(root.left.val, root.right.val)</code>&nbsp;always holds.</p>

<p>Given such a binary tree, you need to output the <b>second minimum</b> value in the set made of all the nodes&#39; value in the whole tree.</p>

<p>If no such second minimum value exists, output -1 instead.</p>

<p>&nbsp;</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt1.jpg" style="width: 431px; height: 302px;" />
<pre>
<strong>Input:</strong> root = [2,2,5,null,null,5,7]
<strong>Output:</strong> 5
<strong>Explanation:</strong> The smallest value is 2, the second smallest value is 5.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2020/10/15/smbt2.jpg" style="width: 321px; height: 182px;" />
<pre>
<strong>Input:</strong> root = [2,2,2]
<strong>Output:</strong> -1
<strong>Explanation:</strong> The smallest value is 2, but there isn&#39;t any second smallest value.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 25]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>root.val == min(root.left.val, root.right.val)</code>&nbsp;for each internal node of the tree.</li>
</ul>



## Solution
### python3
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    root_value = 0
    second_min_value = 2**32

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.root_value = root.val
        def trive(node):
            if not node:
                return
            if node.val != self.root_value:
                if self.second_min_value > node.val:
                    self.second_min_value = node.val
            trive(node.left)
            trive(node.right)
        trive(root)
        return -1 if self.second_min_value == 2**32 else self.second_min_value
```