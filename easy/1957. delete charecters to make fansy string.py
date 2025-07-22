class Solution:
    def makeFancyString(self, s: str) -> str:
        if len(s) < 3:
            return s

        result = s[0:2]  
        for i in range(2, len(s)):
            if s[i] == result[-1] and s[i] == result[-2]:
                continue
            result += s[i]
        return result
