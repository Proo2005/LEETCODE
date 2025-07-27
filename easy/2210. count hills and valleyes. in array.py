class Solution:
    def countHillValley(self, nums: List[int]) -> int:
      
        clean = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i] != nums[i - 1]:
                clean.append(nums[i])

        hills = valleys = 0

        for i in range(1, len(clean) - 1):
            if clean[i] > clean[i - 1] and clean[i] > clean[i + 1]:
                hills += 1
            elif clean[i] < clean[i - 1] and clean[i] < clean[i + 1]:
                valleys += 1

        return hills + valleys
