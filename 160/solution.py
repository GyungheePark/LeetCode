# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
        
        cur = headA
        while cur:
            cur.val = (cur.val, True)
            cur = cur.next
        
        result = None
        cur = headB
        while cur:
            if isinstance(cur.val, tuple):
                result = cur
                break
            cur = cur.next
        
        cur = headA
        while cur:
            cur.val = cur.val[0]
            cur = cur.next
        return result
