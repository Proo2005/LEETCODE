class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        s = s.replace("-", "").upper()
        
        res = ""
        count = 0
        
        for i in range(len(s)-1, -1, -1):
            res += s[i]
            count += 1
            
            if count == k:
                res += "-"
                count = 0
        
        if res.endswith("-"):
            res = res[:-1]
            
        return res[::-1]