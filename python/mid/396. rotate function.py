class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        total_sum = sum(nums)

        # F(0)
        f = sum(i * num for i, num in enumerate(nums))
        res = f

        for k in range(1, n):
            f = f + total_sum - n * nums[n - k]
            res = max(res, f)

        return res