import math

class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        total_prod = math.prod(nums)
        left_sum = 0
        right_prod = total_prod
        
        for i in range(len(nums)):
            right_prod //= nums[i] if nums[i] != 0 else 1
            
            if left_sum == right_prod:
                return i
            
            left_sum += nums[i]
        
        return -1