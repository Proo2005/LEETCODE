class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mi=0
        max_no=max(nums)
        for i in nums:
            if (i!=max_no) and (i*2) <= max_no:
                mi+=1
        if mi==len(nums)-1:
            return nums.index(max_no)
        else:
            return -1
