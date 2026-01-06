class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if s==goal:
            return True
        for i in range(0,len(s)-1):
            a= s[i+1:]+s[:i+1]
            if goal==a:
                return True
        return False