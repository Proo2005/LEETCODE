class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word.isupper() or word.islower():
            return word.isupper() or word.islower()
        elif word[0].isupper():
            return word[1:].islower()
        elif len(word)==1:
            return True
        elif word[0].islower():
            for i in range(1,len(word)):
                if word[i].isupper():
                    return False
        else :
            return False