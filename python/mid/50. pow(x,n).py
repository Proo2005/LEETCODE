class Solution:
    def myPow(self, x: float, n: int) -> float:
        result = pow(x, n)
        return float(f"{result:.5f}")
