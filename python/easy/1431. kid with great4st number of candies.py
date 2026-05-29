class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        a=[]
        s=max(candies)
        for i in candies:
            if extraCandies+i>=s:
                a.append(True)
            else:
                a.append(False)
        return a