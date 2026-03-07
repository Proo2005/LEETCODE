class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        x, y = 0, 0
        s_rem = []
        g_rem = []

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                x += 1
            else:
                s_rem.append(secret[i])
                g_rem.append(guess[i])

        for ch in set(s_rem):
            y += min(s_rem.count(ch), g_rem.count(ch))

        return str(x) + "A" + str(y) + "B"