class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n,mm=len(s1),len(s2)
        if n>m:
            return False
        a=[0]*26
        m=[0]*26

        for i in range(n):
            a[ord(s1[i])-ord('a')]+=1
            m[ord(s2[i])-ord('a')]+=1
        
        if a==m:
            return True

        for i in range(n,mm):
            m[ord(s2[i])-ord('a')]+=1
            m[ord(s2[i-n])-ord('a')]-=1
            if a==m:
                return True
        return False