class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a=sorted(nums)
        c=[]
        for i in range(len(a)):
            if a[i]==target:
                c.append(i)
        return c