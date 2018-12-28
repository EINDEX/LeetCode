# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        tmp = root
        flag = False
        while not flag:
            if tmp.val < val:
                if tmp.right:
                    tmp = tmp.right
                else:
                    tmp.right = TreeNode(val)
                    flag = True
            else:
                if tmp.left:
                    tmp = tmp.left
                else:
                    tmp.left =  TreeNode(val)
                    flag = True
        return root
        