class Node:
    def __init__(self, v):
        self.val = v
        self.next = []
        self.isend = True
        
class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('$')

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        cur = self.root
        prev = self.root
        i = 0
        while i < len(word):
            for n in cur.next:
                if word[i] == n.val[0]:
                    if word[i:] == n.val:
                        n.isend = True
                        return
                    elif n.val.startswith(word[i:]):
                        newnode = Node(word[i:])
                        newn = Node(n.val[len(word)-i:])
                        newn.next = n.next
                        newnode.next.append(newn)
                        cur.next.remove(n)
                        cur.next.append(newnode)
                        return
                    elif word[i:].startswith(n.val):
                        cur = n
                        i += len(n.val)
                        break
                    else:
                        j = 1
                        while i + j < len(word) and j < len(n.val) and word[i+j] == n.val[j]:
                            j += 1
                        newnode = Node(n.val[:j])
                        newnode.isend = False
                        newn = Node(n.val[j:])
                        newn.next = n.next
                        newnode.next.append(newn)
                        newnode.next.append(Node(word[i+j:]))
                        cur.next.remove(n)
                        cur.next.append(newnode)
                        return
            if cur == prev:
                cur.next.append(Node(word[i:]))
                return
            else:
                prev = cur
        
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        def aux(word, n):
            if n.val == word:
                if n.isend:
                    return True
                else:
                    return False
            else:
                if word.startswith(n.val):
                    for nextn in n.next:
                        if aux(word[len(n.val):], nextn):
                            return True
                    return False
                return False
            
        for n in self.root.next:
            if aux(word, n):
                return True
        return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        def aux(prefix, n):
            if prefix[0] == n.val[0]:
                if prefix == n.val:
                    return True
                elif prefix.startswith(n.val):
                    for nextn in n.next:
                        if aux(prefix[len(n.val):], nextn):
                            return True
                    return False
                elif n.val.startswith(prefix):
                    return True
                else:
                    return False
            else:
                return False
        
        for n in self.root.next:
            if aux(prefix, n):
                return True
        return False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
