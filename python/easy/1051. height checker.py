class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        b=sorted(heights)
        c=0
        for i in range(len(b)):
            if heights[i]!=b[i]:
                c+=1
        return c