class Solution:
    def binaryGap(self, n: int) -> int:
        a=bin(n)[2:]
        b=[]
        for i in range(len(a)):
            if a[i]=="1":
                b.append(i)
        d=0
        for j in range(len(b)-1):
            if abs(b[j]-b[j+1])>d:
                d=abs(b[j]-b[j+1])
        return d