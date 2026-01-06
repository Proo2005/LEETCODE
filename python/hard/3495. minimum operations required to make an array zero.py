from typing import List
import math

class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        def range_cost(l: int, r: int) -> int:
            steps = 0
            k = 0
            while (1 << (2 * k)) <= r: 
                left = max(l, 1 << (2 * k))
                right = min(r, (1 << (2 * (k + 1))) - 1)
                if left <= right:
                    count = right - left + 1
                    steps += count * (k + 1)
                k += 1
            return steps

        total_ops = 0
        for l, r in queries:
            steps_sum = range_cost(l, r)
            total_ops += (steps_sum + 1) // 2
        return total_ops
