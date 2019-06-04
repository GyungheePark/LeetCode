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
        def aux(p, q):
            while p and q:
                if p == q:
                    return p
                p = p.next
                q = q.next
            
        p = head
        q = head
        while p and q and q.next:
            p = p.next
            q = q.next.next
            if p == q:
                return aux(p, head)
        return None
