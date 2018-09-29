# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def _inner(node):
            if not node:
                return 0
            l = _inner(node.left)
            if not l:
                node.left = None
            r = _inner(node.right)
            if not r:
                node.right = None
            return node.val + r + l
        
        _inner(root)
        return root
        