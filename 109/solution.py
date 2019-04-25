# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def helper(head, n):
            if n == 0:
                return None
            elif n == 1:
                return TreeNode(head.val)
            i = 0
            cur = head
            while i < n - 1:
                i += 1
                cur = cur.next
                if i == n/2:
                    mid = cur
            root = TreeNode(mid.val)
            root.left = helper(head, n/2)
            if n % 2 == 0:
                root.right = helper(mid.next, n/2-1)
            else:
                root.right = helper(mid.next, n/2)
            return root
        
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next
        if n == 0:
            return None
        return helper(head, n)
