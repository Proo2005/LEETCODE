class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        re=[]
        for i in range(len(nums)):
            re.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return re
