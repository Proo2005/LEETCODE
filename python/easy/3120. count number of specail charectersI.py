class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        for i in ''.join(set(word)):
            if i.isupper() and i.lower() in ''.join(set(word)):
                c+=1
            elif i.islower() and i.upper() in ''.join(set(word)):
                c+=1
        return c//2