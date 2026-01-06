class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        MOD = 10**9 + 7
        from collections import Counter

        n = len(nums)
        right = Counter(nums)   
        left = Counter()       

        ans = 0

        for j in range(n):
            right[nums[j]] -= 1  

           
            x = nums[j] * 2

           
            count_left = left[x]

          
            count_right = right[x]

            ans = (ans + count_left * count_right) % MOD

         
            left[nums[j]] += 1

        return ans
