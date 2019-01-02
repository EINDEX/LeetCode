# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minCameraCover(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def inner(root):
            if not root.left and not root.right:
                return 1
            a = inner(root.left) if root.left else 0
            b = inner(root.right) if root.right else 0
            if a == 1 or b == 1:
                res[0] += 1
                return 2
            if a == 2 or b == 2:
                return 0
            return 1
        if 1 == inner(root):
            res[0] += 1
        return res[0]
        