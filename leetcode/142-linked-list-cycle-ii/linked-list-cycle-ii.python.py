# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        fast = head
        slow = head
        while fast and slow:
            if slow.next and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
                if fast == slow:
                    break
            else:
                return
        p = head
        while p and slow:
            if p == slow:
                return p
            p = p.next
            slow = slow.next
        return p
            
            
