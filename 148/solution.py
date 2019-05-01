# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def helper(head):
            # sort linked list and return the head and the tail node
            if not head:
                return (None, None)
            
            pval = head.val
            phead = ListNode(head.val)
            ptail = phead
            lhead = None
            rhead = None
            cur = head.next
            while cur:
                if cur.val < pval:
                    if not lhead:
                        lhead = ListNode(cur.val)
                        lcur = lhead
                    else:
                        lcur.next = ListNode(cur.val)
                        lcur = lcur.next
                elif cur.val > pval:
                    if not rhead:
                        rhead = ListNode(cur.val)
                        rcur = rhead
                    else:
                        rcur.next = ListNode(cur.val)
                        rcur = rcur.next
                else:
                    ptail.next = ListNode(cur.val)
                    ptail = ptail.next
                cur = cur.next
            
            lh, lt = helper(lhead)
            rh, rt = helper(rhead)
            if lh and rh:
                lt.next = phead
                ptail.next = rh
                return lh, rt
            elif not lh and rh:
                ptail.next = rh
                return phead, rt
            elif lh and not rh:
                lt.next = phead
                return lh, ptail
            else:
                return phead, ptail
        
        h, t = helper(head)
        return h
