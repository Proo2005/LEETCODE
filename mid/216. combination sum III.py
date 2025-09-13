from itertools import combinations
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        nums = list(range(1, 10))  
        result = []
        for comb in combinations(nums, k):
            if sum(comb) == n:
                result.append(list(comb))
        return result
