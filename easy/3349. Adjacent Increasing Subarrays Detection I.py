class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        n = len(nums)
      
        for a in range(n - 2 * k + 1):
            
            first_inc = all(nums[i] < nums[i + 1] for i in range(a, a + k - 1))
          
            second_inc = all(nums[i] < nums[i + 1] for i in range(a + k, a + 2 * k - 1))
            
            if first_inc and second_inc:
                return True
        return False
