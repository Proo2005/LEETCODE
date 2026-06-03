class Solution:
    def reformat(self, s: str) -> str:

        a, b = "", ""
        for i in s:
            if i.isalpha():
                a += i
            elif i.isdigit():
                b += i

        if abs(len(a) - len(b)) > 1:
            return ""
        

        if len(b) > len(a):
            a, b = b, a
            
   
        c = ""
        x, y = 0, 0
        for i in range(len(s)):
            if i % 2 == 0:
                c += a[x]
                x += 1
            else:
                c += b[y]
                y += 1
        return c
