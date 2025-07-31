class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        b=[]
        c=text.split(' ')
        for i in range(len(c)-2):
            if c[i]==first and c[i+1]==second:
                b.append(c[i+2])
        return b