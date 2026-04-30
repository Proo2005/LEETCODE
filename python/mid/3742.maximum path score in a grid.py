from math import inf

class Solution:
    def maximumScore(self, grid, k):
        m, n = len(grid), len(grid[0])

        # score and cost mapping
        score_val = {0: 0, 1: 1, 2: 2}
        cost_val  = {0: 0, 1: 1, 2: 1}

        # dp[i][j] = dict {cost: max_score}
        dp = [[{} for _ in range(n)] for _ in range(m)]

        # initialize start
        start_cost = cost_val[grid[0][0]]
        start_score = score_val[grid[0][0]]

        if start_cost <= k:
            dp[0][0][start_cost] = start_score

        for i in range(m):
            for j in range(n):
                if not dp[i][j]:
                    continue

                for cost_so_far, score_so_far in dp[i][j].items():

                    # move right
                    if j + 1 < n:
                        nc = cost_so_far + cost_val[grid[i][j+1]]
                        if nc <= k:
                            ns = score_so_far + score_val[grid[i][j+1]]
                            dp[i][j+1][nc] = max(dp[i][j+1].get(nc, -inf), ns)

                    # move down
                    if i + 1 < m:
                        nc = cost_so_far + cost_val[grid[i+1][j]]
                        if nc <= k:
                            ns = score_so_far + score_val[grid[i+1][j]]
                            dp[i+1][j][nc] = max(dp[i+1][j].get(nc, -inf), ns)

        # answer = best score at destination within cost k
        if not dp[m-1][n-1]:
            return -1

        return max(dp[m-1][n-1].values())