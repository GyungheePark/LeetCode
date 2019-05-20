class Node:
    def __init__(self, v):
        self.val = v
        self.next = {}
        self.isend = False
        
class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node('$')

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        cur = self.root
        for c in word:
            if c not in cur.next:
                cur.next[c] = Node(c)
            cur = cur.next[c]
        cur.isend = True
        
    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        def aux(node, word):
            if not word:
                if node.isend:
                    return True
                else:
                    return False
            if word[0] == '.':
                for _, nextn in node.next.items():
                    if aux(nextn, word[1:]):
                        return True
                return False
            else:
                if word[0] in node.next:
                    return aux(node.next[word[0]], word[1:])
                else:
                    return False
        
        return aux(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
