# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        d = {}
        def inner(node, x=0, y=0):
            if not node:
                return
            d.setdefault(x, {})
            d[x].setdefault(y, [])
            d[x][y].append(node.val)
            inner(node.left, x-1, y+1)
            inner(node.right, x+1, y+1)
        inner(root)

        def merge_dict_list(dic):
            res = []
            for i in sorted(dic.keys()):
                res += sorted(dic[i])
            return res
        return [merge_dict_list(d[i]) for i in sorted(d.keys())]