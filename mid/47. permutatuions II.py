class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        unique_perms = set(permutations(nums))  
        return [list(p) for p in unique_perms]