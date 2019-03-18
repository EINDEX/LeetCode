# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaf_list(node):
            if not node:
                return []
            if not node.left and not node.right:
                return [node.val]
            return get_leaf_list(node.left) + get_leaf_list(node.right)
        return get_leaf_list(root1) == get_leaf_list(root2)
