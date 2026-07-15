class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        sorted_list = []
        ans = []

        for x in reversed(nums):
            idx = bisect_left(sorted_list, x)
            ans.append(idx)
            insort(sorted_list, x)

        return ans[::-1]