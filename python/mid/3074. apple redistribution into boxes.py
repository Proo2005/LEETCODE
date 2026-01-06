class Solution:
    def minimumBoxes(self, apple, capacity):
        total_apples = sum(apple)

        capacity.sort(reverse=True)

        used = 0
        current = 0

        for cap in capacity:
            current += cap
            used += 1
            if current >= total_apples:
                return used

        return used
