class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        from collections import Counter
        freq = Counter((num % value + value) % value for num in nums)
        
        mex = 0
        while True:
            r = mex % value
            if freq[r] > 0:
                freq[r] -= 1
                mex += 1
            else:
                break
        return mex
