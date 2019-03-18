# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def inner(l,r):
            if l and r and l.val == r.val:
                return inner(l.right,r.left) and inner(l.left, r.right)
            elif not l and not r:
                return True
            else:
                return False
      
        return inner(root.left, root.right)
