class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        a=0
        for i in range(len(s)-2):
            if len(set(s[i:i+3]))==3:
                a+=1
        return a