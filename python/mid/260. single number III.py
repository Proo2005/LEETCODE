class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        a=[]
        for i in range(len(nums)):
            if nums.count(nums[i])==1:
                a.append(nums[i])
        return a