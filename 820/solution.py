class Solution(object):
    def minimumLengthEncoding(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        left = set(words)
        for word in words:
            for k in range(1, len(word)):
                left.discard(word[k:])
        return sum([len(word) + 1 for word in left])
