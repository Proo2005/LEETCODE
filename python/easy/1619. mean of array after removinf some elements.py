class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort()
        k = len(arr) // 20  
        return sum(arr[k:-k]) / len(arr[k:-k])