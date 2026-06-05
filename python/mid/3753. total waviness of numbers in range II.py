from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:

        def solve(x):
            if x <= 0:
                return 0

            s = str(x)
            n = len(s)

            @lru_cache(None)
            def dp(pos, tight, started, prev2, prev1):
                if pos == n:
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started and d == 0:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            False,
                            -1,
                            -1
                        )

                        total_cnt += cnt
                        total_wavy += wav

                    elif not started:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            -1,
                            d
                        )

                        total_cnt += cnt
                        total_wavy += wav

                    elif prev2 == -1:
                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            prev1,
                            d
                        )

                        total_cnt += cnt
                        total_wavy += wav

                    else:
                        add = 0

                        if prev1 > prev2 and prev1 > d:
                            add = 1
                        elif prev1 < prev2 and prev1 < d:
                            add = 1

                        cnt, wav = dp(
                            pos + 1,
                            ntight,
                            True,
                            prev1,
                            d
                        )

                        total_cnt += cnt
                        total_wavy += wav + add * cnt

                return (total_cnt, total_wavy)

            return dp(0, True, False, -1, -1)[1]

        return solve(num2) - solve(num1 - 1)