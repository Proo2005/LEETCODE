class Solution:
    def findComplement(self, num: int) -> int:
        num_bits = len(bin(num)) - 2  
        mask = (1 << num_bits) - 1
        return num ^ mask