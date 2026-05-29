class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        last_seen = -100000 
        
        for i in range(len(nums)):
            if nums[i] == 1:

                if i - last_seen - 1 < k:
                    return False
    
                last_seen = i
                
        return True
