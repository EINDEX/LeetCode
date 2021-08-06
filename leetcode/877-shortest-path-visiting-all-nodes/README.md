# Shortest Path Visiting All Nodes

## Difficulty
Hard

## Question
<p>You have an undirected, connected graph of <code>n</code> nodes labeled from <code>0</code> to <code>n - 1</code>. You are given an array <code>graph</code> where <code>graph[i]</code> is a list of all the nodes connected with node <code>i</code> by an edge.</p>

<p>Return <em>the length of the shortest path that visits every node</em>. You may start and stop at any node, you may revisit nodes multiple times, and you may reuse edges.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/12/shortest1-graph.jpg" style="width: 222px; height: 183px;" />
<pre>
<strong>Input:</strong> graph = [[1,2,3],[0],[0],[0]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One possible path is [1,0,2,0,3]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/12/shortest2-graph.jpg" style="width: 382px; height: 222px;" />
<pre>
<strong>Input:</strong> graph = [[1],[0,2,4],[1,3,4],[2],[1,2]]
<strong>Output:</strong> 4
<strong>Explanation:</strong> One possible path is [0,1,4,2,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == graph.length</code></li>
	<li><code>1 &lt;= n &lt;= 12</code></li>
	<li><code>0 &lt;= graph[i].length &lt;&nbsp;n</code></li>
	<li><code>graph[i]</code> does not contain <code>i</code>.</li>
	<li>If <code>graph[a]</code> contains <code>b</code>, then <code>graph[b]</code> contains <code>a</code>.</li>
	<li>The input graph is always connected.</li>
</ul>



## Solution
### python3
```python3
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        d = [[n + 1] * n for _ in range(n)]
        for i in range(n):
            for j in graph[i]:
                d[i][j] = 1
        
        # 使用 floyd 算法预处理出所有点对之间的最短路径长度
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    d[i][j] = min(d[i][j], d[i][k] + d[k][j])

        f = [[float("inf")] * (1 << n) for _ in range(n)]
        for mask in range(1, 1 << n):
            # 如果 mask 只包含一个 1，即 mask 是 2 的幂
            if (mask & (mask - 1)) == 0:
                u = bin(mask).count("0") - 1
                f[u][mask] = 0
            else:
                for u in range(n):
                    if mask & (1 << u):
                        for v in range(n):
                            if (mask & (1 << v)) and u != v:
                                f[u][mask] = min(f[u][mask], f[v][mask ^ (1 << u)] + d[v][u])

        ans = min(f[u][(1 << n) - 1] for u in range(n))
        return ans


```