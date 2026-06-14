class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        s=""
        d=0
        for i in range(len(word)):
            if word[i]==ch:
                d=i
                break
        return word[:d+1][::-1]+word[d+1:]