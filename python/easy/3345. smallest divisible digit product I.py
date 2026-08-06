class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def prod(n):
            pr=1
            a=n
            while a>0:
                d=a%10
                pr*=d
                a=a//10
            return pr
        v=n
        while  v<v+10:
            if prod(v)%t==0:
                return v
            v+=1
        return 0