from collections import deque
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        if endWord not in wordList:
            return 0
        dic = {}
        for word in wordList:
            for i in range(len(word)):
                w = word[:i] + "*" + word[i+1:]
                if w in dic:
                    dic[w].append(word)
                else:
                    dic[w] = [word]
        q = deque()
        q.append((beginWord, 1))
        visited = set()
        while q:
            curWord, i = q.popleft()
            visited.add(curWord)
            for j in range(len(curWord)):
                w = curWord[:j] + "*" + curWord[j+1:]
                if w in dic:
                    for nextWord in dic[w]:
                        if nextWord == endWord:
                            return i+1
                        else:
                            if nextWord not in visited:
                                q.append((nextWord, i+1))

        return 0
