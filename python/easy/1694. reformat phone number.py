class Solution:
    def reformatNumber(self, number: str) -> str:
        a = number.replace("-", "").replace(" ", "")
        
        chunks = []
        i = 0
        n = len(a)
        

        while n > 4:
            chunks.append(a[i:i+3])
            i += 3
            n -= 3

        if n == 4:
            chunks.append(a[i:i+2])
            chunks.append(a[i+2:i+4])
        else:
            chunks.append(a[i:])
            

        return "-".join(chunks)
