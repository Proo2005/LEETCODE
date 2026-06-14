class Solution:
    def isThree(self, n: int) -> bool:
        s=0
        for i in range(1,n+1):
            if n%i==0:
                s+=1
        return s==3