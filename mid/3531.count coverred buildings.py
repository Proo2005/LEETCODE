from bisect import bisect_left, bisect_right

class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        rows = {}
        cols = {}

        for x, y in buildings:
            rows.setdefault(x, []).append(y)
            cols.setdefault(y, []).append(x)

        for r in rows:
            rows[r].sort()
        for c in cols:
            cols[c].sort()

        ans = 0

        for x, y in buildings:
            row = rows[x]
            col = cols[y]


            pos_y = bisect_left(row, y)
            left_exists = pos_y > 0

   
            right_exists = pos_y < len(row) - 1

         
            pos_x = bisect_left(col, x)
            up_exists = pos_x > 0


            down_exists = pos_x < len(col) - 1

            if left_exists and right_exists and up_exists and down_exists:
                ans += 1

        return ans
