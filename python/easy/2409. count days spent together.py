class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days_in_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        def date_to_day(date_str: str) -> int:
            month, day = map(int, date_str.split("-"))
            return sum(days_in_months[:month - 1]) + day
        alice_start = date_to_day(arriveAlice)
        alice_end = date_to_day(leaveAlice)
        bob_start = date_to_day(arriveBob)
        bob_end = date_to_day(leaveBob)
        start_overlap = max(alice_start, bob_start)
        end_overlap = min(alice_end, bob_end)
    
        if start_overlap <= end_overlap:
            return end_overlap - start_overlap + 1
        return 0
