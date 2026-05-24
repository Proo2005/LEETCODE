class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = "0"

        for _ in range(1, n):
            inv = ''.join('1' if ch == '0' else '0' for ch in s)
            s = s + "1" + inv[::-1]

        return s[k - 1]