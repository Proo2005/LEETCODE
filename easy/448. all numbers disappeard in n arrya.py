class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for num in nums:
            index = abs(num) - 1
            nums[index] = -abs(nums[index])  
     
        result = [i + 1 for i in range(len(nums)) if nums[i] > 0]
        return result