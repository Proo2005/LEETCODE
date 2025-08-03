class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def no_zero(x: int) -> bool:
            return '0' not in str(x)
        
        for i in range(1, n):
            if no_zero(i) and no_zero(n - i):
                return [i, n - i]
       
        return []
