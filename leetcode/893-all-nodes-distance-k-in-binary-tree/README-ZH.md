# All Nodes Distance K in Binary Tree

## Difficulty
Medium

## Question
<p>Given the <code>root</code> of a binary tree, the value of a target node <code>target</code>, and an integer <code>k</code>, return <em>an array of the values of all nodes that have a distance </em><code>k</code><em> from the target node.</em></p>

<p>You can return the answer in <strong>any order</strong>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/06/28/sketch0.png" style="width: 500px; height: 429px;" />
<pre>
<strong>Input:</strong> root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, k = 2
<strong>Output:</strong> [7,4,1]
Explanation: The nodes that are a distance 2 from the target node (with value 5) have values 7, 4, and 1.
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> root = [1], target = 1, k = 3
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the tree is in the range <code>[1, 500]</code>.</li>
	<li><code>0 &lt;= Node.val &lt;= 500</code></li>
	<li>All the values <code>Node.val</code> are <strong>unique</strong>.</li>
	<li><code>target</code> is the value of one of the nodes in the tree.</li>
	<li><code>0 &lt;= k &lt;= 1000</code></li>
</ul>



## Solution
### python3
```python3
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {} # 邻接矩阵
        # 先遍历树生成邻接矩阵
        # 因为 All the values Node.val are unique.
        # 所以可以直接存储值在邻接矩阵里
        def dfs(node, parent=None):
            if not node:
                return
            graph.setdefault(node.val, [parent.val] if parent else [])
            if parent:
                graph[parent.val].append(node.val)
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root)

        # 从 target 开始遍历邻接矩阵找到值列表
        path = set() # 记录去过的点
        result = []
        def dfs_graph(t, depth):
            if t in path:
                return 
            path.add(t)
            if depth == 0:
                result.append(t)
                return
            for next_target_value in graph[t]:
                dfs_graph(next_target_value, depth-1)

        dfs_graph(target.val, k)
        return result
```