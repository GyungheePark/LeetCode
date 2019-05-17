# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def aux(head):
            if not head.next:
                return (head, head)
            else:
                tmp = head
                (h, t) = aux(head.next)
                t.next = tmp
                return (h, tmp)
            
        if not head:
            return head
        (h, t) = aux(head)
        t.next = None
        return h
