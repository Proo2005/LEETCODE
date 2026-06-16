class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        return sorted(set.intersection(*(set(x) for x in nums)))