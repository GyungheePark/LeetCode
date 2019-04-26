import heapq
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        for i, v in enumerate(lists):
            if v:
                heapq.heappush(h, (v.val, i))
        
        root = None
        while h:
            (v, i) = heapq.heappop(h)
            if lists[i].next:
                heapq.heappush(h, (lists[i].next.val, i))
                lists[i] = lists[i].next
            if not root:
                root = ListNode(v)
                cur = root
            else:
                cur.next = ListNode(v)
                cur = cur.next
                
        return root
