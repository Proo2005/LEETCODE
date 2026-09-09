class Solution:
    def countCommas(self, n: int) -> int:
        total_commas = 0
        thousands = 1000

        while n >= thousands:
            total_commas += (n - thousands + 1)
            thousands *= 1000
            
        return total_commas
