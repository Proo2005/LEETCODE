from collections import Counter
from typing import List

class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        canon = (tuple(sorted(d)) for d in dominoes)
        counts = Counter(canon)
        return sum(v * (v - 1) // 2 for v in counts.values())
