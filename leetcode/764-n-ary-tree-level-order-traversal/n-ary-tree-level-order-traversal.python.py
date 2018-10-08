"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        res = []
        def inner(node, depth=0):
            if not node:
                return
            if len(res) == depth:
                res.append([])
            res[depth].append(node.val)
            if node.children:
                for c in node.children:
                    inner(c, depth+1)
        inner(root)
        return res
        