import math

class Solution:
    def smallestBalancedIndex(self, nums: list[int]) -> int:
        n = len(nums)

        # suffix log product
        suffix_log = [0]*(n+1)
        for i in range(n-1, -1, -1):
            suffix_log[i] = suffix_log[i+1] + math.log(nums[i])

        left_sum = 0

        for i in range(n):
            if left_sum > 0:
                if abs(math.log(left_sum) - suffix_log[i+1]) < 1e-9:
                    return i
            elif suffix_log[i+1] == 0:  # both sides = 0/1 case
                return i

            left_sum += nums[i]

        return -1