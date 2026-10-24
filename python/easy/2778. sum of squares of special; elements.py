class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        n=len(nums)
        c=0
        for i in range(n):
            if n%(i+1)==0:
                c+=nums[i]**2
        return c