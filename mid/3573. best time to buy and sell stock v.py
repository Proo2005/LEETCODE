class Solution:
    def maximumProfit(self, prices: List[int], k: int) -> int:

        n = len(prices)
        INF = float('-inf')

        dp_buy = [INF] * (k + 1)
        dp_sell = [INF] * (k + 1)
        dp_free = [INF] * (k + 1)

        dp_free[0] = 0

        for price in prices:
            for t in range(k, -1, -1):
        
                dp_buy[t] = max(dp_buy[t], dp_free[t] - price)
                dp_sell[t] = max(dp_sell[t], dp_free[t] + price)

                if t + 1 <= k:
                    dp_free[t + 1] = max(
                        dp_free[t + 1],
                        dp_buy[t] + price,
                        dp_sell[t] - price
                    )

        return max(dp_free)
