class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        num_set = set(nums)
        multiple = k
        while True:
            if multiple not in num_set:
                return multiple
            multiple += k
