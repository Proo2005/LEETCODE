from typing import List

class Solution:
    def maximumAmount(self, coins: List[List[int]]) -> int:
        n, m = len(coins), len(coins[0])

        dp = [[[-10**18] * 3 for _ in range(m)] for _ in range(n)]

        for k in range(3):
            if coins[0][0] >= 0:
                dp[0][0][k] = coins[0][0]
            elif k > 0:
                dp[0][0][k] = 0
            else:
                dp[0][0][k] = coins[0][0]

        for i in range(n):
            for j in range(m):
                for k in range(3):
                    if i == 0 and j == 0:
                        continue

                    val = coins[i][j]

              
                    if i > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k] + val)

                        if val < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i-1][j][k-1])

            
                    if j > 0:
                        dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k] + val)

                        if val < 0 and k > 0:
                            dp[i][j][k] = max(dp[i][j][k], dp[i][j-1][k-1])

        return max(dp[n-1][m-1])