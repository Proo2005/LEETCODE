class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        s = 0
        c = len(mat) - 1

        for i in range(len(mat)):
            s += mat[i][i]
            s += mat[i][c]
            c -= 1

        if len(mat) % 2 == 1:
            mid = len(mat) // 2
            s -= mat[mid][mid]

        return s