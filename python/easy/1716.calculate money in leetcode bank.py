class Solution(object):
    def totalMoney(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Each full week contributes a fixed pattern of 7 days
        weeks = n // 7
        days = n % 7
        
        # Total money from full weeks
        # Each week starts with an increasing Monday amount (1, 2, 3, ...)
        total = (weeks * (weeks - 1) // 2) * 7 + weeks * 28
        
        # Remaining days of the last week
        start = weeks + 1
        for i in range(days):
            total += start + i
        
        return total
