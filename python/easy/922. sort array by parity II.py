class Solution:
    def sortArrayByParityII(self, num: List[int]) -> List[int]:
        i, j = 0, 1
        n = len(num)

        while i < n and j < n:
            if num[i] % 2 == 0:
                i += 2
            elif num[j] % 2 == 1:
                j += 2
            else:
                num[i], num[j] = num[j], num[i]
                i += 2
                j += 2

        return num