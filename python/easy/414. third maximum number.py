class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        if len(sorted(set(nums)))<=2:
            return max(nums)
        return sorted(set(nums))[-3]