import math
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def prime(n):
            if n<2:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n%i==0:
                    return False
            return True
        
        s=0
        for i in range(left,right+1):
            if prime((bin(i)[2:]).count("1")):
                s+=1
        return s