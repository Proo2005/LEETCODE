import heapq

class Solution(object):
    def swimInWater(self, grid):
        n = len(grid)
        visited = [[False]*n for _ in range(n)]
        heap = [(grid[0][0], 0, 0)]  
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        visited[0][0] = True
        ans = 0
        
        while heap:
            t, r, c = heapq.heappop(heap)
            ans = max(ans, t)
            if r == n-1 and c == n-1:
                return ans
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and not visited[nr][nc]:
                    visited[nr][nc] = True
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))
