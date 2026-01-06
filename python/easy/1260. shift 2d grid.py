class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        if not grid or not grid[0]:
            return grid
        
        m, n = len(grid), len(grid[0])
        total = m * n
        k %= total  
        
   
        flat = [num for row in grid for num in row]
        if k:
            rotated = flat[-k:] + flat[:-k]
        else:
            rotated = flat
        

        return [rotated[i * n:(i + 1) * n] for i in range(m)]
