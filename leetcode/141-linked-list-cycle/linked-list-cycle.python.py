# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a = head
        b = head
        while a and b:
            a = a.next
            if not b.next:
                return False
            b = b.next.next
            if a == b:
                return True
        return False
            
        