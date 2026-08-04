class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        a=[]
        minel,maxel=min(nums),max(nums)
        for  i in range(minel,maxel+1):
            if i not in nums and i not in a:
                a.append(i)
        return a