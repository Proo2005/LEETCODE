class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        def rotate90(matrix):
            n = len(matrix)

            res = [[0] * n for _ in range(n)]


            for i in range(n):
                for j in range(n):
                    res[j][n - i - 1] = matrix[i][j]

            for i in range(n):
                for j in range(n):
                    matrix[i][j] = res[i][j]
        rotate90(matrix)