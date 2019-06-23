# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        result = head
        cur = head.next
        prevval = head.val
        while cur:
            if prevval <= cur.val:
                prevval = cur.val
                cur = cur.next
                continue
            sortedcur = result
            sortedprev = None
            while sortedcur != cur and sortedcur.val < cur.val:
                sortedprev = sortedcur
                sortedcur = sortedcur.next
            # cur.val < sortedcur.val
            # if sortedprev = None, cur -> sortedcur -> ... -> tmp AND result = cur
            if sortedprev == None:
                tmp = cur.next
                cur.next = sortedcur
                while sortedcur.next != cur:
                    sortedcur = sortedcur.next
                prevval = sortedcur.val
                sortedcur.next = tmp
                result = cur
                cur = tmp
            else: # else, prev -> cur -> sortedcur -> ... -> tmp
                tmp = cur.next
                sortedprev.next = cur
                cur.next = sortedcur
                while sortedcur.next != cur:
                    sortedcur = sortedcur.next
                prevval = sortedcur.val
                sortedcur.next = tmp
                cur = tmp
        return result
