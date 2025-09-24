class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[]
        for i in range(1,len(nums)+1):
            b=sum(nums[:i])
            a.append(b)
        return a
    






class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        a=[nums[0]]
        for i in range(1,len(nums)):
            nums[i]=nums[i]+nums[i-1]
            
        return nums