from itertools import permutations
from itertools import combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        a = [i for i in range(1, n + 1)]
        return [list(c) for c in combinations(a, k)]