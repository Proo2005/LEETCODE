class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a=k
        for i in arr:
            if arr.count(i)==1:
                a-=1
                if a==0:
                    return i
        return ""