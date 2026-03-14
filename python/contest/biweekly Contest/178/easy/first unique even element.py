class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        for i in  nums:
            if nums.count(i)==1 and i%2==0:
                return i
        return -1 