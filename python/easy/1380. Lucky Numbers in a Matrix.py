class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        lucky = []
        
    
        row_mins = [min(row) for row in matrix]
        
   
        col_maxes = [max(col) for col in zip(*matrix)]
        

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == row_mins[r] and matrix[r][c] == col_maxes[c]:
                    lucky.append(matrix[r][c])
        
        return lucky