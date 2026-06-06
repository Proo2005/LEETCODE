class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        a=sorted(arr)
        s=a[1]-a[0]
        for i in range(len(a)-1):
            if a[i+1]-a[i] !=s:
                return False
        return True