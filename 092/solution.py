# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if not head:
            return head
        prevhead = None
        prev = None
        cur = head
        for i in range(m-1):
            node = ListNode(cur.val)
            if i == 0:
                prevhead = node
                prev = prevhead
            else:
                prev.next = node
                prev = prev.next
            cur = cur.next
        revhead = None
        rev = None
        for i in range(n-m+1):
            node = ListNode(cur.val)
            if i == 0:
                revhead = node
                rev = revhead
            else:
                node.next = revhead
                revhead = node
            cur = cur.next
        resulthead = None
        resultlast = None
        if prevhead and revhead:
            resulthead = prevhead
            prev.next = revhead
            resultlast = rev
        elif prevhead and not revhead:
            resulthead = prevhead
            resultlast = prev
        elif not prevhead and revhead:
            resulthead = revhead
            resultlast = rev
        while cur:
            node = ListNode(cur.val)
            if not resulthead:
                resulthead = node
                resultlast = node
            else:
                resultlast.next = node
                resultlast = resultlast.next
            cur = cur.next
        return resulthead
