class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        j=-1
        for i in range(len(s)//2):
            c=s[i]
            s[i]=s[j]
            s[j]=c
            j-=1