class Solution:
    def maxProduct(self, n: int) -> int:
        a=n
        c=[]

        while a>0:
            d=a%10
            c.append(d)
            a=a//10
        return sorted(c)[-1]* sorted(c)[-2]