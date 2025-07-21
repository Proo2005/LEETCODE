class Solution:
    def grayCode(self, n: int) -> List[int]:
        def binary_to_gray(n):
            return n ^ (n >> 1)
        a=[]

        for i in range(1 << n):
            a.append(binary_to_gray(i))
        return a