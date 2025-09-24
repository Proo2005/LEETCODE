class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """
        a=[0]*n
        b=0
        for i in range(n):
            a[i]=start + 2*i
        for j in a:
            b^=j
        return b