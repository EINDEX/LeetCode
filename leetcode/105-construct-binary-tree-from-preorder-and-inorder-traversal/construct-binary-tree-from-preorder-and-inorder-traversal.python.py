# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None
        
        root = TreeNode(preorder[0])
        l = inorder.index(root.val)
        r = len(inorder) - l - 1
        if l:
            root.left = self.buildTree(preorder[1:1+l],inorder[:l])
        if r:
            root.right = self.buildTree(preorder[-r:],inorder[-r:])
        return root
            
        
