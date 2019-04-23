class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                result.append([1,1])
            else:
                row = []
                for j in range(i+1):
                    if j == 0:
                        row.append(1)
                    elif j == i:
                        row.append(1)
                    else:
                        row.append(result[i-1][j-1] + result[i-1][j])
                result.append(row)
        return result
