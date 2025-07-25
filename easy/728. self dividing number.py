class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        a=[]
        for i in range(left,right+1):
            s=str(i)
            b=0
            if '0' not in s:
                for j in s:
                    if int(s)%int(j)==0:
                        b+=1
            if b==len(s):
                a.append(int(i))
        return a

