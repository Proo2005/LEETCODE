from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, indexDiff, valueDiff):
        window = SortedList()

        for i, num in enumerate(nums):
            pos = window.bisect_left(num)

            if pos < len(window) and abs(window[pos] - num) <= valueDiff:
                return True

            if pos > 0 and abs(window[pos-1] - num) <= valueDiff:
                return True

            window.add(num)

            if len(window) > indexDiff:
                window.remove(nums[i-indexDiff])

        return False