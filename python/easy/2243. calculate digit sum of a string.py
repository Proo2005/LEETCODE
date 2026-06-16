class Solution:
    def digitSum(self, s: str, k: int) -> str:
        a = s

        while len(a) > k:
            d = ""

            for i in range(0, len(a), k):
                b = a[i:i+k]

                su = 0
                for ch in b:
                    su += int(ch)

                d += str(su)

            a = d

        return a