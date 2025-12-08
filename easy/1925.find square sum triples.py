class Solution:
    def countTriples(self, n: int) -> int:
        count = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                c_sq = i*i + j*j
                c = int(c_sq ** 0.5)
                if c*c == c_sq and c <= n:
                    count += 1
        return count
