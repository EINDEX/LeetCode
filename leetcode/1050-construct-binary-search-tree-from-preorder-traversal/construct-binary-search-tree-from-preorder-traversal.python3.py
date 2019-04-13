# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        
        def inner(l):
            if not l:
                return None
            t = TreeNode(l[0])
            t.left = inner([x for x in l if x <l[0]])
            t.right = inner([x for x in l if x >l[0]])
            return t
        return inner(preorder)