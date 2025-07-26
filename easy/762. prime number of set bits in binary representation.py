import math

class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        def is_prime(n):
            if n < 2:
                return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0:
                    return False
            return True
        
        counter = 0
        for j in range(left, right + 1):
            ones_count = bin(j).count('1')
            if is_prime(ones_count):
                counter += 1
        return counter
