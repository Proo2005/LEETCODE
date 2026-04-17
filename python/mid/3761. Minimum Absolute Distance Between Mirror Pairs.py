from typing import List

class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        index_map = {}
        min_dist = float('inf')

        for i, num in enumerate(nums):
            if num in index_map:
                min_dist = min(min_dist, i - index_map[num])

            rev = int(str(num)[::-1])
            index_map[rev] = i

        return min_dist if min_dist != float('inf') else -1