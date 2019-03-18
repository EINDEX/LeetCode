# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        res = []
        def inner(x, node):
            x = x * 10 + node.val
            if node.left:
                inner(x, node.left)
            if node.right:
                inner(x, node.right)
            if not node.left and not node.right:
                res.append(x)
       
        inner(0, root)
        return sum(res)
