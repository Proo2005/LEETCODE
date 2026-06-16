class Solution:
    def processStr(self, s: str) -> str:
        result=""
        for i in s:
            if i.islower():
                result+=i
            elif i=="*":
                result=result[:-1]
            elif i=="#":
                result=result*2
            elif i=="%":
                result=result[::-1]
        return result