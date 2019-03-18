# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        def inner(path, node):
            if not node:
                return
            path = path[:]
            path.append(str(node.val))
            if not node.left and not node.right:
                res.append(path)
            inner(path, node.left)
            inner(path, node.right)
        inner([], root)
        return ['->'.join(p) for p in res]
        
