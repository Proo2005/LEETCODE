from typing import List

class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        arr = []
        
        # Step 1: Flatten grid
        for row in grid:
            for val in row:
                arr.append(val)
        
        # Step 2: Check feasibility
        rem = arr[0] % x
        for num in arr:
            if num % x != rem:
                return -1
        
        # Step 3: Sort
        arr.sort()
        
        # Step 4: Choose median
        median = arr[len(arr) // 2]
        
        # Step 5: Count operations
        ops = 0
        for num in arr:
            ops += abs(num - median) // x
        
        return ops