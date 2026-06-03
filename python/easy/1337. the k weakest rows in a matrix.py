class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        a={}
        for idx, row in enumerate(mat):
            
            a[idx] = row.count(1)
        sorted_rows = sorted(a.items(), key=lambda item: item[1])
        return [idx for idx, count in sorted_rows[:k]]
        