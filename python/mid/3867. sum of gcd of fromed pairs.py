import math

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        n = len(nums)
        prefixGcd = []
        mx = 0
  
        for x in nums:
            mx = max(mx, x)
            prefixGcd.append(math.gcd(x, mx))

        prefixGcd.sort()
        ans = 0
        left, right = 0, n - 1
        
        while left < right:
            ans += math.gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
            
        return ans
