from collections import Counter

class Solution:
    def maximumTotalDamage(self, power):
        freq = Counter(power)
        unique = sorted(freq.keys())
        n = len(unique)
        total = [freq[x] * x for x in unique]

        dp = [0] * n
        dp[0] = total[0]

        for i in range(1, n):
 
            j = i - 1
            while j >= 0 and unique[i] - unique[j] <= 2:
                j -= 1

            include = total[i] + (dp[j] if j >= 0 else 0)
            exclude = dp[i-1]
            dp[i] = max(include, exclude)

        return dp[-1]
