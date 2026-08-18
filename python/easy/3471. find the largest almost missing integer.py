class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        subarray_counts = defaultdict(int)
        n = len(nums)
        for j in range(n - k + 1):
            current_window = set(nums[j:j+k])
            for num in current_window:
                subarray_counts[num] += 1
        best_num = -1 
        
        for num, count in subarray_counts.items():
            pass
            
        return best_num
