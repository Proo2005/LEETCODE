from collections import deque

class Solution:
    def hasValidPath(self, grid):
        m, n = len(grid), len(grid[0])

        # directions: (dx, dy)
        dirs = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        # check if two cells connect
        def is_valid(x1, y1, x2, y2):
            if not (0 <= x2 < m and 0 <= y2 < n):
                return False
            for dx, dy in dirs[grid[x2][y2]]:
                if x2 + dx == x1 and y2 + dy == y1:
                    return True
            return False

        q = deque([(0, 0)])
        visited = set([(0, 0)])

        while q:
            x, y = q.popleft()

            if (x, y) == (m - 1, n - 1):
                return True

            for dx, dy in dirs[grid[x][y]]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited and is_valid(x, y, nx, ny):
                    visited.add((nx, ny))
                    q.append((nx, ny))

        return False