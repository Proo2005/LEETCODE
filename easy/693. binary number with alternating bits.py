class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        c = bin(n)[2:] 
      

        for i in range(len(c) - 1):
            if c[i]==c[i+1]:
                return False
        return True