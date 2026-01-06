from collections import Counter
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        freq = Counter(nums)
        result = []
        for num, count in freq.items():
            if count > n // 3:  
                result.append(num)
        return result
