class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            row = {"1":False, "2":False, "3":False, "4":False, "5":False, "6":False, "7":False, "8":False, "9":False}
            col = {"1":False, "2":False, "3":False, "4":False, "5":False, "6":False, "7":False, "8":False, "9":False}
            sub = {"1":False, "2":False, "3":False, "4":False, "5":False, "6":False, "7":False, "8":False, "9":False}
            for j in range(9):
                if board[i][j] != ".":
                    if row[board[i][j]]:
                        return False
                    else:
                        row[board[i][j]] = True
                if board[j][i] != ".":
                    if col[board[j][i]]:
                        return False
                    else:
                        col[board[j][i]] = True
                if board[i/3*3+j/3][i%3*3+j%3] != ".":
                    if sub[board[i/3*3+j/3][i%3*3+j%3]]:
                        return False
                    else:
                        sub[board[i/3*3+j/3][i%3*3+j%3]] = True
        return True
