class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
    
  
        for col in range(n):
            val = matrix[0][col]
            i, j = 0, col
            while i < m and j < n:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1

   
        for row in range(1, m):
            val = matrix[row][0]
            i, j = row, 0
            while i < m and j < n:
                if matrix[i][j] != val:
                    return False
                i += 1
                j += 1

        return True
