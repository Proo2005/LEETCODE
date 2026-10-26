class Solution:
    def countIslands(self, grid: List[List[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        valid_islands = 0
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def get_island_sum(start_r, start_c):
            queue = deque([(start_r, start_c)])
            visited.add((start_r, start_c))
            
            island_sum = 0
            
            while queue:
                r, c = queue.popleft()
                island_sum += grid[r][c]  
                
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < rows and 
                        0 <= nc < cols and 
                        grid[nr][nc] > 0 and 
                        (nr, nc) not in visited):
                        
                        queue.append((nr, nc))
                        visited.add((nr, nc)) 
            
            return island_sum
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0 and (r, c) not in visited:
                    total_value = get_island_sum(r, c)
                    if total_value % k == 0:
                        valid_islands += 1
                        
        return valid_islands
