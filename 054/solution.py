class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if matrix == []:
            return []
        
        result = []
        i = 0
        j = 0
        m = len(matrix)
        n = len(matrix[0])
        while True:
            result.append(matrix[i][j])
            matrix[i][j] = "o"
            if (j == 0 or matrix[i][j-1] == "o") and (i == 0 or matrix[i-1][j] == "o"):
                if j < n - 1 and matrix[i][j+1] != "o":
                    j += 1
                elif i < m - 1 and matrix[i+1][j] != "o":
                    i += 1
                else:
                    break
            elif (j == n - 1 or matrix[i][j+1] == "o") and (i == 0 or matrix[i-1][j] == "o"):
                if i < m - 1 and matrix[i+1][j] != "o":
                    i += 1
                elif j > 0 and matrix[i][j-1] != "o":
                    j -= 1
                else:
                    break
            elif (j == n - 1 or matrix[i][j+1] == "o") and (i == m-1 or matrix[i+1][j] == "o"):
                if j > 0 and matrix[i][j-1] != "o":
                    j -= 1
                elif i > 0 and matrix[i-1][j] != "o":
                    i -= 1
                else:
                    break
            else:
                if i > 0 and matrix[i-1][j] != "o":
                    i -= 1
                elif j < n - 1 and matrix[i][j+1] != "o":
                    j += 1
                else:
                    break
        return result
