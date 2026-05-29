class Solution:
    def minElement(self, nums: List[int]) -> int:
        def s(n):
            a=n
            su=0
            while a>0:
                d=a%10
                su+=d
                a=a//10
            return su

        b = float('inf')
        for i in nums:
            if s(i)<b:
                b=s(i)
        return b

