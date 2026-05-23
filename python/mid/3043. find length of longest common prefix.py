class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixes = set()

        # store all prefixes from arr1
        for x in arr1:
            s = str(x)

            for i in range(1, len(s) + 1):
                prefixes.add(s[:i])

        ans = 0

        # check prefixes in arr2
        for x in arr2:
            s = str(x)

            for i in range(1, len(s) + 1):
                if s[:i] in prefixes:
                    ans = max(ans, i)

        return ans