from functools import lru_cache

class Solution:
    def tribonacci(self, n: int) -> int:
        @lru_cache(None)
        def tribo(k):
            if k == 0:
                return 0
            if k == 1 or k == 2:
                return 1
            return tribo(k - 1) + tribo(k - 2) + tribo(k - 3)
        return tribo(n)
s