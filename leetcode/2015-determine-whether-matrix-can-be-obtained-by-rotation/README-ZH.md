# Determine Whether Matrix Can Be Obtained By Rotation

## Difficulty
Easy

## Question
<p>Given two <code>n x n</code> binary matrices <code>mat</code> and <code>target</code>, return <code>true</code><em> if it is possible to make </em><code>mat</code><em> equal to </em><code>target</code><em> by <strong>rotating</strong> </em><code>mat</code><em> in <strong>90-degree increments</strong>, or </em><code>false</code><em> otherwise.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid3.png" style="width: 301px; height: 121px;" />
<pre>
<strong>Input:</strong> mat = [[0,1],[1,0]], target = [[1,0],[0,1]]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can rotate mat 90 degrees clockwise to make mat equal target.
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/20/grid4.png" style="width: 301px; height: 121px;" />
<pre>
<strong>Input:</strong> mat = [[0,1],[1,1]], target = [[1,0],[0,1]]
<strong>Output:</strong> false
<strong>Explanation:</strong> It is impossible to make mat equal to target by rotating mat.
</pre>

<p><strong>Example 3:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/05/26/grid4.png" style="width: 661px; height: 184px;" />
<pre>
<strong>Input:</strong> mat = [[0,0,0],[0,1,0],[1,1,1]], target = [[1,1,1],[0,1,0],[0,0,0]]
<strong>Output:</strong> true
<strong>Explanation: </strong>We can rotate mat 90 degrees clockwise two times to make mat equal target.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == mat.length == target.length</code></li>
	<li><code>n == mat[i].length == target[i].length</code></li>
	<li><code>1 &lt;= n &lt;= 10</code></li>
	<li><code>mat[i][j]</code> and <code>target[i][j]</code> are either <code>0</code> or <code>1</code>.</li>
</ul>


## Solution
### python3
```python3
class Solution:
    
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        s_mat = lambda x: sum([sum(l) for l in mat])
        if s_mat(mat) != s_mat(target):
            return False
        
        def rotate(matrix):
            h, w = len(matrix), len(matrix[0]) #矩阵旋转必然是方阵，所以此处可以只求一个
            #沿对角线对称
            for i in range(h):
                for j in range(i, h): #注意此处只对矩阵右半部分操作，否则会重复换位
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

            #水平方向翻转

            for i in range(h):
                start = 0
                end = h-1
                while start<end:
                    matrix[i][start], matrix[i][end] = matrix[i][end], matrix[i][start]
                    start+=1
                    end-=1

        def compare(mat, target):
            for x in range(len(mat)):
                for y in range(len(mat[0])):
                    if mat[x][y] != target[x][y]:
                        return False
            return True
        
        if compare(mat, target):
            return True
        print(mat)
        print(target)
        for _ in range(3):
            rotate(mat)
            print(mat)
            print(target)
            if compare(mat, target):
                return True
        return False
            
        
```

## Author
EINDEX