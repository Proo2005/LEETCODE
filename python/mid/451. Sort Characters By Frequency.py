class Solution:
    def frequencySort(self, s: str) -> str:
        a={}
        for i in s:
            if i not in a:
                a[i]= s.count(i)
        sorted_chars = sorted(a.keys(), key=lambda x: a[x], reverse=True)
        aa=""
        for i in sorted_chars:
            aa+=i*s.count(i)
        return aa