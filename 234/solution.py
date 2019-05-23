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
        s = []
        cur = head
        while cur:
            s.append(cur.val)
            cur = cur.next
        if s == s[::-1]:
            return True
        else:
            return False
