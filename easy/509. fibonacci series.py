class Solution:
    def fib(self, n: int) -> int:

        def g(n):
            if n==1 or n==0:
                return n
            for i in range(n):
                return g(n-1) +g(n-2)
        return g(n)