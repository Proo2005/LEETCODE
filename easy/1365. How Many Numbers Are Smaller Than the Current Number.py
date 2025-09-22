class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        c=0
        b=0
        a=[]
        for i in range(len(nums)):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    c+=1
            
            for k in range(i+1,len(nums)):
                if nums[k]<nums[i]:
                    b+=1

            a.append(c+b)
            c=0
            b=0
        return a