# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        if not head:
            return result
        oddtail = head
        if not head.next:
            return result
        evenhead = head.next
        eventail = head.next
        
        nextodd = eventail.next
        if nextodd:
            nexteven = nextodd.next
        else:
            nexteven = None
            
        while nextodd:
            tmp = nextodd
            if nextodd.next:
                nextodd = nextodd.next.next
            else:
                nextodd = None
            oddtail.next = tmp
            oddtail = oddtail.next
            oddtail.next = evenhead
            eventail.next = nextodd
            if nexteven:
                tmp = nexteven
                if nexteven.next:
                    nexteven = nexteven.next.next
                else:
                    nexteven = None
                eventail.next = tmp
                eventail = eventail.next
                eventail.next = nextodd

        return result
