class Solution:
    def minOperations(self, s: str) -> int:
        arr = list(s)
        target = sorted(arr)

        if arr == target[::-1]:
            return -1

        swaps = 0
        n = len(arr)

        for i in range(n):
            if arr[i] != target[i]:
                j = i
                while arr[j] != target[i]:
                    j += 1
                while j > i:
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    swaps += 1
                    j -= 1

        return swaps