class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        b = []

        for i in range(len(matrix[0])):
            a = []
            for j in range(len(matrix)):
                a.append(matrix[j][i])
            b.append(a)

        return b