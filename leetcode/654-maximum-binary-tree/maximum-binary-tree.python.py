class Solution:
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums:
            max_num = max(nums)
            i =  nums.index(max_num)
            tree = TreeNode(max_num)
            tree.left = self.constructMaximumBinaryTree(nums[:i])
            if i +1 < len(nums):
                tree.right = self.constructMaximumBinaryTree(nums[i+1:])
            return tree
        

