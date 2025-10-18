class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        intervals = sorted([(num - k, num + k) for num in nums], key=lambda x: x[1])
        
        used = -10**18
        count = 0
        
        for start, end in intervals:
            if used < start:
                used = start
                count += 1
            elif used < end:
                used += 1
                count += 1
        return count
