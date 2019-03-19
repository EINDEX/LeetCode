# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        s = [0]
        def inner(node):
            if not node:
                return
            inner(node.right)
            node.val += s[0]
            s[0] = node.val
            inner(node.left)
            
        
        inner(root)
        return root
        