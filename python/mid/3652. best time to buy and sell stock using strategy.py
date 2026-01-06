class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:

        n = len(prices)

      
        base_profit = sum(strategy[i] * prices[i] for i in range(n))

       
        strat_sum = [0] * (n + 1)
        price_sum = [0] * (n + 1)

        for i in range(n):
            strat_sum[i + 1] = strat_sum[i] + strategy[i] * prices[i]
            price_sum[i + 1] = price_sum[i] + prices[i]

        best_gain = 0
        half = k // 2

        for i in range(n - k + 1):
    
            orig = strat_sum[i + k] - strat_sum[i]

         
            new = price_sum[i + k] - price_sum[i + half]

            best_gain = max(best_gain, new - orig)

        return base_profit + best_gain
