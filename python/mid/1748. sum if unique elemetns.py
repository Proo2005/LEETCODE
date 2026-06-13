class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        if len(set(nums))==len(nums):
            return sum(nums)
        s=0
        for i in nums:
            if nums.count(i)==1:
                s+=i
        return s