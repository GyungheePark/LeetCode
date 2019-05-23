# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        
        if n == 1:
            return True
        
        m = n/2
        prev = None
        cur = head
        while m > 0:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
            m -= 1
        if n % 2 == 1:
            cur = cur.next
        while cur:
            if cur.val == prev.val:
                cur = cur.next
                prev = prev.next
            else:
                return False
        return True
