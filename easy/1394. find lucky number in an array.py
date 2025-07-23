class Solution:
    def findLucky(self, arr: List[int]) -> int:
        a=[]
        for i in arr:
            if arr.count(i)==i:
                a.append(i)
        if a:
            return (max(a))
        else:
            return -1
        
        