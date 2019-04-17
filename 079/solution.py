import copy
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        def getAdj(n, m, i, j):
            adjs = []
            if i > 0:
                adjs.append((i-1, j))
            if i < n-1:
                adjs.append((i+1, j))
            if j > 0:
                adjs.append((i, j-1))
            if j < m-1:
                adjs.append((i, j+1))
            return adjs

        def dfs(board, visited, word, i, j):
            if len(word) == 1:
                return True
            visited.append((i,j))
            n = len(board)
            m = len(board[0])
            adjs = getAdj(n, m, i, j)
            for (i1, j1) in adjs:
                if board[i1][j1] == word[1] and (i1, j1) not in visited:
                    if dfs(board, list(visited), word[1:], i1, j1):
                        return True
            return False

        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    visited = []
                    if dfs(board, visited, word, i, j):
                        return True
        return False
