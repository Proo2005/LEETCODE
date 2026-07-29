from collections import Counter
from math import factorial

class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        cnt = Counter(s)

        half = [0] * 26
        mid = ""

        for ch, f in cnt.items():
            if f & 1:
                mid = ch
            half[ord(ch) - 97] = f // 2

        m = sum(half)

        fact = [1] * (m + 1)
        for i in range(1, m + 1):
            fact[i] = fact[i - 1] * i

        cur = fact[m]
        for f in half:
            cur //= fact[f]

        if cur < k:
            return ""

        ans = []

        while m:
            for c in range(26):
                if half[c] == 0:
                    continue

                nxt = cur * half[c] // m

                if nxt >= k:
                    ans.append(chr(c + 97))
                    cur = nxt
                    half[c] -= 1
                    m -= 1
                    break
                else:
                    k -= nxt

        first = "".join(ans)
        return first + mid + first[::-1]