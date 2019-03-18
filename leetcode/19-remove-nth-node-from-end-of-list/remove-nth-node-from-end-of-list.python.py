# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        second = None
        first = head
        p = 0
        while first.next:
            first = first.next
            p += 1
            if p == n:
                second = head
            elif p > n:
                second = second.next
        if second:
            second.next = second.next.next
        elif head.next:
            head = head.next
        else:
            return None
        return head
        
        
