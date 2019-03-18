# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        def inner(node, depth=0):
            if not node:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            inner(node.left, depth+1)
            inner(node.right, depth+1)
        inner(root)
        return res[::-1]
        
