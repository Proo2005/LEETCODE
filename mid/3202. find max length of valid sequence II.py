class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        dp=[[0]*k for _ in range (k)]
        ans=0
        for num in nums:
            r = num % k
            for y in range(k):
                dp[r][y] = dp[y][r] + 1
                ans = max(ans, dp[r][y])
        return ans