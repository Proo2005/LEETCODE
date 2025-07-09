class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
 
        m,n=len(mat),len(mat[0])
        total = m * n
        if total != r * c:
            return mat

        flat = [num for row in mat for num in row]
        reshaped = []
        for i in range(r):
            reshaped.append(flat[i * c : (i + 1) * c])
        
        return reshaped