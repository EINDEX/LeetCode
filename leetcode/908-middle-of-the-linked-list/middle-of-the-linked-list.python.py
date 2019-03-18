# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return
        fast = head
        slow = head
        while fast.next:
            fast = fast.next
            slow = slow.next
            if fast.next:
                fast = fast.next
            else:
                break
        return slow
        
