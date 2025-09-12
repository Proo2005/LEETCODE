class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD = 10**9 + 7
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for day in range(2, n + 1):
           
            for j in range(1, day):
                if j + delay <= day <= j + forget - 1:
                    dp[day] = (dp[day] + dp[j]) % MOD
        
        
        result = 0
        for day in range(1, n + 1):
            if day + forget > n:
                result = (result + dp[day]) % MOD
        
        return result