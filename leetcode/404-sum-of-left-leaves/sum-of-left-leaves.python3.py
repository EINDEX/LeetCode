# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _inner(root, is_left):
            if not root:
                return 0
            if is_left and not root.left and not root.right:
                return root.val
            x = 0
            return x + _inner(root.left, True) + _inner(root.right, False)
        return _inner(root, False)
