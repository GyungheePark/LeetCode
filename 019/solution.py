# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromFront(self, head, n):
        if n == 0:
            return head.next
        else:
            head.next = self.removeNthFromFront(head.next, n-1)
            return head
        
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        size = 0
        node = head
        while node:
            size += 1
            node = node.next
        return self.removeNthFromFront(head, size - n)
