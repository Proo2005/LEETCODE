from typing import List

class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        m = len(mat[0])

        for i in range(len(mat)):
            shift = k % m

            if i % 2 == 0:
                shifted = mat[i][shift:] + mat[i][:shift]  
            else:
                shifted = mat[i][-shift:] + mat[i][:-shift] 

            if shifted != mat[i]:
                return False

        return True