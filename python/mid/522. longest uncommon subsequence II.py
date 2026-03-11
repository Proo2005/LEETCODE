from typing import List
from collections import Counter

class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        
        def is_subsequence(a, b):
            i = 0
            for c in b:
                if i < len(a) and a[i] == c:
                    i += 1
            return i == len(a)

        count = Counter(strs)

        strs.sort(key=len, reverse=True)

        for i, s in enumerate(strs):
            if count[s] > 1:
                continue

            if all(not is_subsequence(s, t) for j, t in enumerate(strs) if i != j):
                return len(s)

        return -1