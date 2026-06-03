class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        a=sorted(nums)
        for i in range(len(a)-1,-1,-1):
            if sum(a[i:])>sum(a[:i]):
                return a[i:][::-1]