class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)

        dp = [0] * (n + 3)
  
        for i in range(n - 1, -1, -1):
            max_margin = float('-inf')
            take_sum = 0
            
     
            for k in range(1, 4):
                if i + k <= n:
                    take_sum += stoneValue[i + k - 1]
           
                    current_margin = take_sum - dp[i + k]
                    if current_margin > max_margin:
                        max_margin = current_margin
            
            dp[i] = max_margin
     
        if dp[0] > 0:
            return "Alice"
        elif dp[0] < 0:
            return "Bob"
        else:
            return "Tie"
