# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
BIG_VALIE = 2**31

class Solution:

    root_value = 0
    second_min_value = BIG_VALIE

    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.root_value = root.val
        def trive(node):
            if not node:
                return
            if node.val != self.root_value:
                if self.second_min_value > node.val:
                    self.second_min_value = node.val
                return
            trive(node.left)
            trive(node.right)
        trive(root)
        return -1 if self.second_min_value == BIG_VALIE else self.second_min_value