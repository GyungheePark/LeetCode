class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        def dfs(board, i, j):
            board[i][j] = '_'
            n = len(board)
            m = len(board[0])
            if i > 0 and board[i-1][j] == 'O':
                dfs(board, i-1, j)
            if i < n-1 and board[i+1][j] == 'O':
                dfs(board, i+1, j)
            if j > 0 and board[i][j-1] == 'O':
                dfs(board, i, j-1)
            if j < m-1 and board[i][j+1] == 'O':
                dfs(board, i, j+1)
        
        if not board or not board[0]:
            return
        
        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if (i == 0 or i == n-1 or j == 0 or j == m-1) and board[i][j] == 'O':
                    dfs(board, i, j)
                    
        for i in range(n):
            for j in range(m):
                if board[i][j] == '_':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
