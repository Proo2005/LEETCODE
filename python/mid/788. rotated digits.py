
class Solution:
    def rotatedDigits(self, n: int) -> int:
        a=[2,5,6,9]
        c=0
        for i in range(1,n+1):
            for j in str(i):
                if int(j) in a:
                    c+=1
        return c 