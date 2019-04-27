# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverseFirstK(head, k):
            if k == 0:
                return (None, None, None)
            elif k == 1:
                return (head, head, head.next)

            cur = head
            short = False
            for i in range(k-1):
                if not cur:
                    short = True
                    break
                prev = cur
                cur = cur.next
            if short or not cur:
                return head, head, head.next
            prev.next = cur.next
            cur.next, prevrest, rest = reverseFirstK(head, k-1)
            return cur, prevrest, rest
        
        if not head:
            return head
        head, prevrest, rest = reverseFirstK(head, k)
        result = head
        while result != prevrest and rest:
            prev = prevrest
            result, prevrest, rest = reverseFirstK(rest,k)
            prev.next = result
        return head
