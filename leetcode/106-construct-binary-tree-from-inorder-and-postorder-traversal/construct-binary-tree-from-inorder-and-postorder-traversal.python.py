# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not postorder:
            return None
        
        root = TreeNode(postorder[-1])
        l = inorder.index(root.val)
        r = len(inorder) - l - 1
        if l:
            root.left = self.buildTree(inorder[:l], postorder[:l])
        if r:
            root.right = self.buildTree(inorder[l+1:], postorder[l:l+r])
        return root
            
        
