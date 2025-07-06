class Solution:
    def countBits(self, n: int) -> List[int]:
        c=[]
        
        for i in range(n+1):   
            a=(str(bin(i))[2:]).count('1')
            c.append(a)
        
        return c
