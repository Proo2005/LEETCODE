class Solution:
    def maxSum(self, nums: List[int]) -> int:
        unique_positives = set()
        total = 0
        for num in nums:
            if num > 0 and num not in unique_positives:
                unique_positives.add(num)
                total += num
        if total > 0:
            return total
        else:
            return max(nums)
      