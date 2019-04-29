from collections import deque
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head
        newhead = Node(head.val, head.next, head.random)
        cur = head
        newcur = newhead
        q = deque()
        q.append((cur, newcur))
        dic = {}
        while q:
            cur, newcur = q.popleft()
            dic[cur] = newcur
            if cur.next:
                if cur.next in dic:
                    newcur.next = dic[cur.next]
                else:
                    newcur.next = Node(cur.next.val, cur.next.next, cur.next.random)
                    q.append((cur.next, newcur.next))
                    dic[cur.next] = newcur.next
            if cur.random:
                if cur.random in dic:
                    newcur.random = dic[cur.random]
                else:
                    newcur.random = Node(cur.random.val, cur.random.next, cur.random.random)
                    q.append((cur.random, newcur.random))
                    dic[cur.random] = newcur.random
        return newhead
