from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if nums.count(val) > 1:
            k = 0
            for i in range(len(nums)):
                if nums[i] != val:
                    nums[k] = nums[i]
                    k += 1
            return k
        else:
     
            return len(nums)
        