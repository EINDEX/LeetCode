# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = None
        p = None
        flag = 0
        while l1 and l2:
            t = l1.val + l2.val + flag
            if not p:
                p = ListNode(t%10)
            else:
                p.next = ListNode(t%10)
                p = p.next
            if not head:
                head = p
            flag = t // 10
            l1 = l1.next
            l2 = l2.next
        if l1 or l2 or flag:
            if l1:
                p.next = l1
            elif l2:
                p.next = l2
            else:
                p.next = None
            
            while p.next or flag:
                if  p.next:
                    t =  p.next.val + flag
                    p.next.val = t % 10
                else:
                    t = flag
                    p.next = ListNode(t%10)
                flag = t // 10
                p =  p.next
        return head
