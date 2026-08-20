class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        if len(nums)<=2:
            return nums
        arr1=[nums[0]]
        arr2=[nums[1]]
        currel=2

        for i in range(2,len(nums)):
            if arr1[-1]>arr2[-1]:
                arr1.append(nums[currel])
                currel+=1
            else:
                arr2.append(nums[currel])
                currel+=1
        return arr1+arr2