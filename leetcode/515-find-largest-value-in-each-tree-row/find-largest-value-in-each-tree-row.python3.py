# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        res = []
        def inner(node, depth=1):
            if not node:
                return
            if len(res) < depth:
                res.append(node.val)
            else:
                res[depth-1] = max(res[depth-1], node.val)
            inner(node.left,depth+1)
            inner(node.right,depth+1)
        inner(root)
        return res
        