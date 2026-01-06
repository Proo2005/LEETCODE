class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        b = ''  
        c=[]
        for i in nums:
            b += str(i)  
            c.append(int(b,2)%5==0)
        return c
