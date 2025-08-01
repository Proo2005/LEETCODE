class Solution:
    def dayOfYear(self, date: str) -> int:
        months = {
            1: 31, 2: 28, 3: 31, 4: 30,
            5: 31, 6: 30, 7: 31, 8: 31,
            9: 30, 10: 31, 11: 30, 12: 31,
        }

        def is_leap(year):
            return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

        year = int(date[0:4])
        month = int(date[5:7])
        day = int(date[8:10])

        total = 0
        for i in range(1, month):
            total += months[i]

       
        if month > 2 and is_leap(year):
            total += 1

        total += day
        return total
