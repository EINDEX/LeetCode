# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def get_path(path, node, target):
            path.append(node)
            if node.val == target.val:
                return path
            elif node.val > target.val:
                return get_path(path, node.left, target)
            else:
                return get_path(path, node.right, target)
        
        p1 = get_path([], root, p)
        p2 = get_path([], root, q)
        x = 0
        while len(p1) > x and len(p2) > x:
            if p1[x].val != p2[x].val:
                break
            x += 1
        return p1[x-1]
            