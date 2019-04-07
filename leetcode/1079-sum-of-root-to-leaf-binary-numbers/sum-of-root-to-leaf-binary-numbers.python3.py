# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        res = []
        m = 10**9 + 7
        if not root:
            return 0
        
        def inner(node, value):
            if not node:
                return
            if value is None:
                new_value = node.val
            else:
                new_value = (value << 1) + node.val
            if not node.left and not node.right:
                res.append(new_value)
                return
            inner(node.left,new_value)
            inner(node.right,new_value)
        inner(root, None)
        return int(sum([x for x in res])) % m