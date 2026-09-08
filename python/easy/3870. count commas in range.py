class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0
            
        total_commas = 0
        # Add commas contributed by all numbers up to the largest power of 10 below n
        s = str(n)
        length = len(s)
        
        # Sum up commas for all fully completed digit ranges (e.g., 4-digit numbers, 5-digit numbers...)
        for i in range(4, length):
            # There are 9 * 10**(i-1) numbers with exactly i digits
            # Each has (i - 1) // 3 commas
            total_commas += (9 * (10 ** (i - 1))) * ((i - 1) // 3)
            
        # Add commas for the remaining numbers with exactly 'length' digits
        lower_bound = 10 ** (length - 1)
        remaining_numbers = n - lower_bound + 1
        total_commas += remaining_numbers * ((length - 1) // 3)
        
        return total_commas
