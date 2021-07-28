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