from typing import List

class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        n = len(heights)
        result = [0] * n
        stack = [] 
        for i in range(n - 1, -1, -1):
            current_height = heights[i]
            visible_count = 0
            while stack and stack[-1] < current_height:
                stack.pop()
                visible_count += 1
            if stack:
                visible_count += 1
            result[i] = visible_count
            stack.append(current_height)
            
        return result
