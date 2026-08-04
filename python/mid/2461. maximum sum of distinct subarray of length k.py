    from collections import Counter
from typing import List

class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        max_sum = 0
        current_sum = 0
        num_counts = Counter() 
        
        for i, num in enumerate(nums):
            current_sum += num
            num_counts[num] += 1
            if i >= k:
                outgoing_num = nums[i - k]
                current_sum -= outgoing_num
                num_counts[outgoing_num] -= 1
                if num_counts[outgoing_num] == 0:
                    del num_counts[outgoing_num]
            if i >= k - 1 and len(num_counts) == k:
                max_sum = max(max_sum, current_sum)
                
        return max_sum
