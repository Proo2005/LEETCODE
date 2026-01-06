class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        # Zeller's Congruence for Gregorian calendar
        if month <= 2:
            month += 12
            year -= 1
        q = day
        m = month
        K = year % 100
        J = year // 100
        h = (q + (13 * (m + 1)) // 5 + K + K // 4 + J // 4 + 5 * J) % 7
        
        mapping = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        return mapping[h]

