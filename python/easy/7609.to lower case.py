
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
    




##   or 




class Solution:
    def toLowerCase(self, s: str) -> str:
        a=''
        for i in s:
            if ord(i)>=65 and ord(i)<=90:
                a+=chr(ord(i)+32)
            else:
                a+=i
        return a
