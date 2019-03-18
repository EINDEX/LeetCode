# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return 0
        if L <= root.val <= R:
            res = root.val
        else:
            res = 0
        res += self.rangeSumBST(root.left,L,R)
        res += self.rangeSumBST(root.right,L,R)
        return res
        
            
            
        
