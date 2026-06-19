class Solution:
    def countEven(self, num: int) -> int:
        def get_digit_sum(n):
            digit_sum = 0
            while n > 0:
                digit_sum += n % 10
                n //= 10
            return digit_sum

        count = 0
    
        for j in range(1, num + 1):
     
            if get_digit_sum(j) % 2 == 0:
                count += 1
                
        return count
