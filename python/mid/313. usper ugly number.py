class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        k = len(primes)
        idx = [0] * k
        ugly = [1] * n

        for i in range(1, n):
            next_vals = [primes[j] * ugly[idx[j]] for j in range(k)]
            next_ugly = min(next_vals)

            ugly[i] = next_ugly

            for j in range(k):
                if next_vals[j] == next_ugly:
                    idx[j] += 1

        return ugly[-1]