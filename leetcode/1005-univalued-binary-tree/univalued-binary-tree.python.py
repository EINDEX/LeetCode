# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inner(root, val):
            if not root:
                return True
            if root.val!= val:
                return False
            return inner(root.left, val) and inner(root.right, val)
        
        return inner(root, root.val)
            
        
