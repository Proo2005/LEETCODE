from collections import defaultdict

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        pos = defaultdict(list)

     
        for i, x in enumerate(nums):
            pos[x].append(i)

        ans = [0] * len(nums)

     
        for indices in pos.values():
            n = len(indices)

            prefix = [0]
            for x in indices:
                prefix.append(prefix[-1] + x)

            for i, idx in enumerate(indices):
                left = idx * i - prefix[i]
                right = (prefix[n] - prefix[i + 1]) - idx * (n - i - 1)

                ans[idx] = left + right

        return ans