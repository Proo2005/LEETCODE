class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        if len(coordinates) <= 2:
            return True

        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        dx = x1 - x0
        dy = y1 - y0

        for x, y in coordinates[2:]:
           
            if dy * (x - x0) != dx * (y - y0):
                return False
        return True
