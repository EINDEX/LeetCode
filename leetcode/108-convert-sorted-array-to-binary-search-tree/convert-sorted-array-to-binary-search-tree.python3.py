# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        def inner(nums):
            if not nums:
                return None
            mid = len(nums)//2
            node = TreeNode(nums[mid])
            print(nums[:mid],nums[mid] ,nums[mid+1:])
            node.left = inner(nums[:mid])
            node.right = inner(nums[mid+1:])
            return node
        return inner(nums)
        