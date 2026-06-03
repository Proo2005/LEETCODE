class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        rs,ms=0,0
        for i in nums:
            rs+=i
            if rs<ms:
                ms=rs
        return 1-ms