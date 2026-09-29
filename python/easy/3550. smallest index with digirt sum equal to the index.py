class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        def c(n):
            a=n
            s=0
            while a:
                d=a%10
                s+=d
                a=a//10
            return s
        for i in range(len(nums)):
            if c(nums[i])==i:
                return i
        return -1