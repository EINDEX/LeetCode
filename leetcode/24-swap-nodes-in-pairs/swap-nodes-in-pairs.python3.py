# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head and head.next:
            t = self.swapPairs(head.next.next)
        else:
            return head
        # print(t.val)
        a = head
        b = head.next
        b.next = a
        a.next = t
        return b