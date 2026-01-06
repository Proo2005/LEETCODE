from collections import Counter

class Solution:
    def findXSum(self, nums, k, x):
        n = len(nums)
        ans = []

        for i in range(n - k + 1):
            sub = nums[i:i + k]
            count = Counter(sub)
            
            # Sort by frequency descending, then by value descending
            sorted_items = sorted(count.items(), key=lambda item: (-item[1], -item[0]))
            
            # Pick top x elements and compute their contribution
            total = 0
            for j in range(min(x, len(sorted_items))):
                num, freq = sorted_items[j]
                total += num * freq
            
            ans.append(total)
        return ans
