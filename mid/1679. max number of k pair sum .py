from collections import Counter

class Solution:
    def maxOperations(self, nums: list[int], k: int) -> int:
        count = Counter(nums)
        operations = 0
        
        for num in list(count.keys()):
            complement = k - num
            if num == complement:
                operations += count[num] // 2
            else:
                pair_ops = min(count[num], count[complement])
                operations += pair_ops
                count[num] -= pair_ops
                count[complement] -= pair_ops
                
        return operations
