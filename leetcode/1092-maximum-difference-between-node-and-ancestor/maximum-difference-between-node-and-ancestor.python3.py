# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        res = [0]
        def inner(node, M,m):
            if not node:
                r = abs(M-m)
                if r >res[0]:
                    res[0] = r
                return
            if node.val > M:
                M = node.val
            if node.val < m:
                m = node.val
            inner(node.left, M, m)
            inner(node.right, M, m)
            
        inner(root, -1,100001)
        return res[0]
        