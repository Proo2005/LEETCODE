class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0 

        nums.sort()
        max_gap = 0
        for i in range(1, n):
            max_gap = max(max_gap, nums[i] - nums[i-1])
        return max_gap
