from typing import List
import math

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0

        for n in nums:
            divs = set()
            for i in range(1, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    divs.add(i)
                    divs.add(n // i)
                if len(divs) > 4:
                    break

            if len(divs) == 4:
                total += sum(divs)

        return total
