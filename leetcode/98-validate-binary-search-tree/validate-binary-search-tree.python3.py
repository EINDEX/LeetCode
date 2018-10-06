# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def inner(node, l=None, h=None):
            if not node:
                return True
            res = True
            if l is not None and h is not None:
                res = l < node.val < h
            elif l is not None:
                res = l < node.val
            elif h is not None:
                res = node.val < h
            if not res:
                return res
            
            return inner(node.left, l=l, h=node.val) and inner(node.right, l=node.val, h=h)
        return inner(root)
            
            
                
            
        