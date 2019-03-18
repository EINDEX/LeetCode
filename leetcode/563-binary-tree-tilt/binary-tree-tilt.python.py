# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _inner(root):
            res = 0
            if not root:
                res += 0
                return 0, 0
            else:
                l, rl = _inner(root.left)
                r, rr = _inner(root.right)
                res += rl
                res += rr
                return root.val + l + r, abs(l-r) + res
        return _inner(root)[1]

