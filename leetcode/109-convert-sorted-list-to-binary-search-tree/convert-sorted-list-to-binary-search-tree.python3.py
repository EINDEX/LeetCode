# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        a, b, c= head, head, None
        while b.next:
            c = a
            a = a.next
            if b.next.next:
                b = b.next.next
            else:
                b = b.next
                break
        if c:
            c.next = None
        node = TreeNode(a.val)
        node.right = self.sortedListToBST(a.next)
        node.left = self.sortedListToBST(head)
        return node
                
            
            
        