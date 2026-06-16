class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:

        for x in range(left, right + 1):
            ok = False

            for l, r in ranges:
                if l <= x <= r:
                    ok = True
                    break

            if not ok:
                return False

        return True