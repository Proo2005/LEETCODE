class Solution:
    def largestInteger(self, num: int) -> int:
        digits = list(map(int, str(num)))

        even = sorted([x for x in digits if x % 2 == 0], reverse=True)
        odd = sorted([x for x in digits if x % 2 == 1], reverse=True)

        e = o = 0
        ans = 0

        for d in digits:
            if d % 2 == 0:
                ans = ans * 10 + even[e]
                e += 1
            else:
                ans = ans * 10 + odd[o]
                o += 1

        return ans