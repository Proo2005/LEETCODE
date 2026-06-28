from collections import Counter

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        cnt = Counter()

        for i in range(len(s) - 9):
            cnt[s[i:i+10]] += 1

        ans = []

        for seq, freq in cnt.items():
            if freq > 1:
                ans.append(seq)

        return ans