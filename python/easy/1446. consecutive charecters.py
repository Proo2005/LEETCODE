class Solution:
    def maxPower(self, s: str) -> int:
        c=0
        for i in  range(len(s)):
            ss=0
            for j in range(i+1,len(s)):
                if s[j]==s[i]:
                    ss+=1
                else:
                    break
            c=max(ss,c)
        return c+1
            