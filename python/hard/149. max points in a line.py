from collections import defaultdict
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) <= 2:
            return len(points)

        result = 0

        for i in range(len(points)):
            slopes = defaultdict(int)

            for j in range(i+1, len(points)):
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]

                if dx == 0:
                    slope = "inf"
                else:
                    slope = dy / dx

                slopes[slope] += 1
                result = max(result, slopes[slope] + 1)

        return result