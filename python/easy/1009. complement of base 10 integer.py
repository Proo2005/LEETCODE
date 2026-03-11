class Solution:
    def bitwiseComplement(self, n: int) -> int:
        a=""
        for i in bin(n)[2:]:
            if  i == "1":
                a+="0"
            else:
                a+="1"
        return int(a,2)
