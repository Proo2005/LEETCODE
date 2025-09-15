class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        a = len(text.split())
        broken = set(brokenLetters)  

        for i in text.split():
          
            if any(ch in broken for ch in i):
                a -= 1

        return a
