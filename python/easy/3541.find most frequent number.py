class Solution:
    def maxFreqSum(self, s: str) -> int:
 
        a=0
        b=0
        for i in s:
            if i in "AEIOUaeiou":
                if s.count(i)>a:
                    a=s.count(i)
            else:
                if s.count(i)>b:
                    b=s.count(i)
        return a+b