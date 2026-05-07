class Solution:
    def maxValue(self, nums: List[int]) -> List[int]:
        n = len(nums)

        suf = [0] * n
        suf[-1] = nums[-1]

        for i in range(n - 2, -1, -1):
            suf[i] = min(suf[i + 1], nums[i])

        ans = [0] * n

        start = 0
        pref_max = nums[0]

        for i in range(n - 1):
            pref_max = max(pref_max, nums[i])

      
            if pref_max <= suf[i + 1]:
                mx = max(nums[start:i + 1])

                for j in range(start, i + 1):
                    ans[j] = mx

                start = i + 1


        mx = max(nums[start:])

        for j in range(start, n):
            ans[j] = mx

        return ans