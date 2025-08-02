class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        a={}
        for i in arr:
            a[i]=arr.count(i)
        return (sorted(a.values())==sorted(set(a.values())))