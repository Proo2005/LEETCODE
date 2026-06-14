class Solution:
    def getLucky(self, s: str, k: int) -> int:

        def ss(n):
            sm = 0
            while n > 0:
                sm += n % 10
                n //= 10
            return sm

        d = ""

        for ch in s:
            d += str(ord(ch) - ord('a') + 1)

        ans = 0

        for x in d:
            ans += int(x)

        for _ in range(k - 1):
            ans = ss(ans)

        return ans