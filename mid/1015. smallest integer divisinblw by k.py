class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        c=1
        for i in range(k):
            if c%k == 0:
                return i+1
            c=c*10 +1
        return -1