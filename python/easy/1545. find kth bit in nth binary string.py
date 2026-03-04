class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def invert(a):
            r=""
            for i in a:
                if i=="1":
                    r+="0"
                else:
                    r+="1"
            return r

        a="0"
        for i in range(n):
            a=a+"1"+invert(a)[::-1]
        return a[k-1]
