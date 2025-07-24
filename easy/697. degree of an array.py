class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left = {}    
        right = {}    
        count = {}   

        for i, num in enumerate(nums):
            if num not in left:
                left[num] = i
            right[num] = i
            count[num] = count.get(num, 0) + 1

        degree = max(count.values())
        min_len = len(nums)

        for num in count:
            if count[num] == degree:
                length = right[num] - left[num] + 1
                min_len = min(min_len, length)

        return min_len
