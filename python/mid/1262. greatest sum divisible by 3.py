class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        total = sum(nums)
        
        if total % 3 == 0:
            return total
        
        r1 = sorted([x for x in nums if x % 3 == 1])
        r2 = sorted([x for x in nums if x % 3 == 2])
        
        ans = 0
        
        if total % 3 == 1:
            remove1 = r1[0] if r1 else float('inf')
            remove2 = r2[0] + r2[1] if len(r2) >= 2 else float('inf')
            ans = total - min(remove1, remove2)
        
        else:   
            remove1 = r2[0] if r2 else float('inf')
            remove2 = r1[0] + r1[1] if len(r1) >= 2 else float('inf')
            ans = total - min(remove1, remove2)
        
        return ans
