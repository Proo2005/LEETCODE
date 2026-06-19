class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        a=len(pref)
        c=0
        for i in words :
            if i[:a]==pref:
                c+=1
        return c